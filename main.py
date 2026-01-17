#!/usr/bin/env python3
"""
Color Blast - A colorful puzzle game for Android
Version: 1.0.0
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import random
from enum import Enum

# Configure window
Window.size = (540, 960)
Window.clearcolor = (0.95, 0.95, 0.97, 1)


class GameState(Enum):
    """Game state enumeration"""
    MENU = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3


class ColorBlock(Widget):
    """Individual color block in the game"""
    color = ListProperty([1, 1, 1, 1])
    is_selected = ListProperty([0.8, 0.8, 0.8, 1])
    
    def __init__(self, color_value, pos, **kwargs):
        super().__init__(**kwargs)
        self.color_value = color_value
        self.set_color(color_value)
        self.size_hint = (0.2, 0.2)
        self.selected = False
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        
    def set_color(self, color_value):
        """Set block color based on value"""
        colors = {
            0: [1, 0.2, 0.2, 1],      # Red
            1: [0.2, 0.7, 1, 1],      # Blue
            2: [0.2, 1, 0.4, 1],      # Green
            3: [1, 1, 0.2, 1],        # Yellow
            4: [1, 0.6, 0.2, 1],      # Orange
            5: [1, 0.2, 0.8, 1],      # Purple
        }
        self.color_value = color_value
        self.color = colors.get(color_value, [1, 1, 1, 1])
        
    def update_canvas(self, *args):
        """Update canvas drawing"""
        self.canvas.clear()
        with self.canvas:
            if self.selected:
                Color(self.color[0] * 0.7, self.color[1] * 0.7, self.color[2] * 0.7, 1)
            else:
                Color(*self.color)
            Rectangle(pos=self.pos, size=self.size)
            
            # Draw border
            Color(0.3, 0.3, 0.3, 0.5)
            Line(rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1]), width=1)
            
    def on_touch_down(self, touch):
        """Handle touch"""
        if self.collide_point(*touch.pos):
            self.selected = not self.selected
            self.update_canvas()
            return True
        return super().on_touch_down(touch)


class GameBoard(GridLayout):
    """Main game board"""
    score = NumericProperty(0)
    level = NumericProperty(1)
    moves_left = NumericProperty(20)
    
    def __init__(self, **kwargs):
        super().__init__(cols=5, rows=6, spacing=5, padding=10, **kwargs)
        self.size_hint = (1, 0.7)
        self.blocks = []
        self.selected_blocks = []
        self.generate_board()
        
    def generate_board(self):
        """Generate initial game board"""
        self.clear_widgets()
        self.blocks = []
        
        for i in range(30):
            color = random.randint(0, 5)
            block = ColorBlock(color, (0, 0))
            self.add_widget(block)
            self.blocks.append(block)
            
    def check_matches(self):
        """Check for color matches"""
        selected = [b for b in self.blocks if b.selected]
        
        if len(selected) < 2:
            return 0
        
        # Check if all selected blocks have same color
        first_color = selected[0].color_value
        if all(b.color_value == first_color for b in selected):
            points = len(selected) * 10
            self.score += points
            
            # Remove matched blocks
            for block in selected:
                self.remove_widget(block)
                self.blocks.remove(block)
                
            # Fill empty spaces
            self.fill_board()
            self.moves_left -= 1
            return points
        else:
            # Deselect blocks
            for block in selected:
                block.selected = False
                block.update_canvas()
            return 0
            
    def fill_board(self):
        """Fill empty spaces with new blocks"""
        while len(self.blocks) < 30:
            color = random.randint(0, 5)
            block = ColorBlock(color, (0, 0))
            self.add_widget(block)
            self.blocks.append(block)


class GameUI(BoxLayout):
    """Game UI container"""
    
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)
        
        # Header with score and level
        header = BoxLayout(size_hint_y=0.15, spacing=10)
        self.score_label = Label(text='Score: 0', font_size='20sp', bold=True)
        self.level_label = Label(text='Level: 1', font_size='20sp', bold=True)
        self.moves_label = Label(text='Moves: 20', font_size='20sp', bold=True)
        
        header.add_widget(self.score_label)
        header.add_widget(self.level_label)
        header.add_widget(self.moves_label)
        
        self.add_widget(header)
        
        # Game board
        self.game_board = GameBoard()
        self.game_board.bind(score=self.update_score)
        self.game_board.bind(moves_left=self.update_moves)
        self.add_widget(self.game_board)
        
        # Control buttons
        controls = BoxLayout(size_hint_y=0.12, spacing=10)
        match_btn = Button(text='Match', font_size='16sp', background_color=(0.2, 0.7, 1, 1))
        match_btn.bind(on_press=self.on_match_press)
        
        clear_btn = Button(text='Clear', font_size='16sp', background_color=(1, 0.6, 0.2, 1))
        clear_btn.bind(on_press=self.on_clear_press)
        
        controls.add_widget(match_btn)
        controls.add_widget(clear_btn)
        
        self.add_widget(controls)
        
    def on_match_press(self, instance):
        """Handle match button press"""
        self.game_board.check_matches()
        
    def on_clear_press(self, instance):
        """Clear selection"""
        for block in self.game_board.blocks:
            block.selected = False
            block.update_canvas()
            
    def update_score(self, instance, value):
        """Update score display"""
        self.score_label.text = f'Score: {value}'
        
    def update_moves(self, instance, value):
        """Update moves display"""
        self.moves_label.text = f'Moves: {value}'


class ColorBlastApp(App):
    """Main application class"""
    
    def build(self):
        """Build the app"""
        self.title = 'Color Blast'
        self.icon = 'data/icon.png'  # Will be created
        
        root = BoxLayout(orientation='vertical')
        self.game_ui = GameUI()
        root.add_widget(self.game_ui)
        
        return root


if __name__ == '__main__':
    ColorBlastApp().run()
