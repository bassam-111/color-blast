from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.animation import Animation
import random


class ColorBlock(Button):
    """A single colored block in the game grid."""
    
    COLORS = [
        (1, 0, 0, 1),      # Red
        (0, 1, 0, 1),      # Green
        (0, 0, 1, 1),      # Blue
        (1, 1, 0, 1),      # Yellow
        (1, 0, 1, 1),      # Magenta
        (0, 1, 1, 1),      # Cyan
    ]
    
    def __init__(self, color_index, row, col, **kwargs):
        super().__init__(**kwargs)
        self.color_index = color_index
        self.row = row
        self.col = col
        self.selected = False
        self.background_color = self.COLORS[color_index]
        self.background_normal = ''
        self.background_down = ''
        
    def toggle_select(self):
        """Toggle selection state with visual feedback."""
        self.selected = not self.selected
        if self.selected:
            # Make selected blocks slightly darker
            orig_color = self.COLORS[self.color_index]
            self.background_color = (orig_color[0] * 0.7, orig_color[1] * 0.7, 
                                    orig_color[2] * 0.7, 1)
        else:
            self.background_color = self.COLORS[self.color_index]


class GameBoard(GridLayout):
    """The main game board containing the 5x6 grid of blocks."""
    
    ROWS = 6
    COLS = 5
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = self.COLS
        self.rows = self.ROWS
        self.spacing = 2
        self.blocks = []
        self.selected_blocks = []
        self.game_ref = None
        
        self.create_board()
        
    def create_board(self):
        """Create the initial game board with random colored blocks."""
        self.clear_widgets()
        self.blocks = []
        
        for row in range(self.ROWS):
            row_blocks = []
            for col in range(self.COLS):
                color_index = random.randint(0, len(ColorBlock.COLORS) - 1)
                block = ColorBlock(color_index, row, col)
                block.bind(on_press=self.on_block_press)
                self.add_widget(block)
                row_blocks.append(block)
            self.blocks.append(row_blocks)
    
    def on_block_press(self, block):
        """Handle block selection and matching."""
        if not self.game_ref:
            return
            
        # Start new selection
        if not self.selected_blocks:
            self.selected_blocks = []
            self.find_connected_blocks(block.row, block.col, block.color_index)
            
            # Only allow selection if at least 2 blocks match
            if len(self.selected_blocks) >= 2:
                for b in self.selected_blocks:
                    b.toggle_select()
            else:
                self.selected_blocks = []
        else:
            # Remove selected blocks
            self.remove_selected_blocks()
    
    def find_connected_blocks(self, row, col, color_index):
        """Find all connected blocks of the same color using flood fill."""
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return
        
        block = self.blocks[row][col]
        
        if block in self.selected_blocks or block.color_index != color_index:
            return
        
        self.selected_blocks.append(block)
        
        # Check all four directions
        self.find_connected_blocks(row - 1, col, color_index)  # Up
        self.find_connected_blocks(row + 1, col, color_index)  # Down
        self.find_connected_blocks(row, col - 1, color_index)  # Left
        self.find_connected_blocks(row, col + 1, color_index)  # Right
    
    def remove_selected_blocks(self):
        """Remove selected blocks and update score."""
        if not self.selected_blocks:
            return
        
        # Calculate score
        points = len(self.selected_blocks) * 10
        self.game_ref.add_score(points)
        self.game_ref.increment_moves()
        
        # Mark blocks for removal before animation
        blocks_to_remove = list(self.selected_blocks)
        for block in blocks_to_remove:
            block.color_index = -1  # Mark as removed
        
        # Remove blocks with animation
        for block in blocks_to_remove:
            anim = Animation(opacity=0, duration=0.3)
            anim.start(block)
        
        # Schedule block removal and gravity
        Clock.schedule_once(lambda dt: self.apply_gravity(), 0.3)
        
        self.selected_blocks = []
    
    def apply_gravity(self):
        """Make blocks fall down to fill empty spaces."""
        
        # Apply gravity column by column
        for col in range(self.COLS):
            # Collect non-empty blocks from bottom to top
            non_empty = []
            for row in range(self.ROWS - 1, -1, -1):
                block = self.blocks[row][col]
                if block.color_index != -1:
                    non_empty.append(block)
            
            # Refill column from bottom
            row_idx = self.ROWS - 1
            for block in non_empty:
                if block.row != row_idx:
                    # Move block to new position
                    old_row = block.row
                    block.row = row_idx
                    self.blocks[old_row][col] = None
                    self.blocks[row_idx][col] = block
                row_idx -= 1
            
            # Fill remaining spaces with new blocks
            while row_idx >= 0:
                old_block = self.blocks[row_idx][col]
                color_index = random.randint(0, len(ColorBlock.COLORS) - 1)
                new_block = ColorBlock(color_index, row_idx, col)
                new_block.bind(on_press=self.on_block_press)
                new_block.opacity = 0
                
                # Replace widget
                self.remove_widget(old_block)
                self.add_widget(new_block)
                self.blocks[row_idx][col] = new_block
                
                # Animate new block
                anim = Animation(opacity=1, duration=0.3)
                anim.start(new_block)
                
                row_idx -= 1
        
        # Check if level is complete
        self.game_ref.check_level_complete()
    
    def reset_board(self):
        """Reset the board for a new game."""
        self.selected_blocks = []
        self.create_board()


class ColorBlastGame(BoxLayout):
    """Main game container with score, moves, and level display."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        
        self.score = 0
        self.moves = 0
        self.level = 1
        self.target_score = 500
        
        # Create UI
        self.create_ui()
    
    def create_ui(self):
        """Create the game UI layout."""
        # Header with game info
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        
        self.score_label = Label(text=f'Score: {self.score}', 
                                 font_size='20sp', bold=True)
        self.moves_label = Label(text=f'Moves: {self.moves}', 
                                 font_size='20sp', bold=True)
        self.level_label = Label(text=f'Level: {self.level}', 
                                 font_size='20sp', bold=True)
        
        header.add_widget(self.score_label)
        header.add_widget(self.moves_label)
        header.add_widget(self.level_label)
        
        self.add_widget(header)
        
        # Target score display
        self.target_label = Label(text=f'Target: {self.target_score}', 
                                  size_hint=(1, 0.05), font_size='16sp')
        self.add_widget(self.target_label)
        
        # Game board
        self.board = GameBoard(size_hint=(1, 0.75))
        self.board.game_ref = self
        self.add_widget(self.board)
        
        # Buttons
        button_layout = BoxLayout(orientation='horizontal', 
                                 size_hint=(1, 0.1), spacing=10)
        
        reset_btn = Button(text='New Game', font_size='18sp', bold=True)
        reset_btn.bind(on_press=self.reset_game)
        button_layout.add_widget(reset_btn)
        
        self.add_widget(button_layout)
    
    def add_score(self, points):
        """Add points to the score."""
        self.score += points
        self.score_label.text = f'Score: {self.score}'
    
    def increment_moves(self):
        """Increment the move counter."""
        self.moves += 1
        self.moves_label.text = f'Moves: {self.moves}'
    
    def check_level_complete(self):
        """Check if the player has reached the target score."""
        if self.score >= self.target_score:
            self.level_up()
    
    def level_up(self):
        """Progress to the next level."""
        self.level += 1
        self.target_score = self.level * 500
        self.level_label.text = f'Level: {self.level}'
        self.target_label.text = f'Target: {self.target_score}'
        
        # Show level complete message
        self.target_label.text = f'Level {self.level - 1} Complete! Target: {self.target_score}'
        Clock.schedule_once(
            lambda dt: setattr(self.target_label, 'text', f'Target: {self.target_score}'), 
            2
        )
    
    def reset_game(self, instance):
        """Reset the game to initial state."""
        self.score = 0
        self.moves = 0
        self.level = 1
        self.target_score = 500
        
        self.score_label.text = f'Score: {self.score}'
        self.moves_label.text = f'Moves: {self.moves}'
        self.level_label.text = f'Level: {self.level}'
        self.target_label.text = f'Target: {self.target_score}'
        
        self.board.reset_board()


class ColorBlastApp(App):
    """Main Kivy application."""
    
    def build(self):
        return ColorBlastGame()


if __name__ == '__main__':
    ColorBlastApp().run()
