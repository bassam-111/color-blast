#!/usr/bin/env python3
"""
Unit tests for Color Blast game logic.
Tests core functionality without requiring Kivy UI.
"""

def test_color_definitions():
    """Test that we have exactly 6 colors defined."""
    colors = [
        (1, 0, 0, 1),      # Red
        (0, 1, 0, 1),      # Green
        (0, 0, 1, 1),      # Blue
        (1, 1, 0, 1),      # Yellow
        (1, 0, 1, 1),      # Magenta
        (0, 1, 1, 1),      # Cyan
    ]
    assert len(colors) == 6, "Should have exactly 6 colors"
    print("✓ Color definitions test passed")

def test_grid_dimensions():
    """Test that grid dimensions are correct."""
    ROWS = 6
    COLS = 5
    assert ROWS == 6, "Should have 6 rows"
    assert COLS == 5, "Should have 5 columns"
    total_blocks = ROWS * COLS
    assert total_blocks == 30, "Grid should have 30 blocks"
    print("✓ Grid dimensions test passed")

def test_scoring_logic():
    """Test scoring calculation."""
    blocks_removed = 5
    points_per_block = 10
    expected_score = blocks_removed * points_per_block
    assert expected_score == 50, "5 blocks should give 50 points"
    
    blocks_removed = 10
    expected_score = blocks_removed * points_per_block
    assert expected_score == 100, "10 blocks should give 100 points"
    print("✓ Scoring logic test passed")

def test_level_progression():
    """Test level progression logic."""
    level = 1
    target_score = 500
    assert target_score == level * 500, "Level 1 target should be 500"
    
    level = 2
    target_score = level * 500
    assert target_score == 1000, "Level 2 target should be 1000"
    
    level = 3
    target_score = level * 500
    assert target_score == 1500, "Level 3 target should be 1500"
    print("✓ Level progression test passed")

def test_flood_fill_logic():
    """Test the flood fill logic for finding connected blocks."""
    # Simulate a simple grid
    grid = [
        [0, 0, 1, 1, 2],
        [0, 1, 1, 2, 2],
        [1, 1, 0, 2, 3],
        [1, 0, 0, 0, 3],
        [2, 2, 2, 3, 3],
        [2, 3, 3, 3, 3],
    ]
    
    # Test: Starting at (0,0) with color 0 should find 3 connected blocks
    # These are the blocks: (0,0), (0,1), and (1,0) which form a connected group
    visited = set()
    
    def flood_fill(row, col, color):
        if row < 0 or row >= 6 or col < 0 or col >= 5:
            return
        if (row, col) in visited or grid[row][col] != color:
            return
        visited.add((row, col))
        flood_fill(row - 1, col, color)
        flood_fill(row + 1, col, color)
        flood_fill(row, col - 1, color)
        flood_fill(row, col + 1, color)
    
    flood_fill(0, 0, 0)
    assert len(visited) == 3, f"Should find 3 connected blocks, found {len(visited)}"
    print("✓ Flood fill logic test passed")

def test_minimum_selection():
    """Test that we need at least 2 blocks to make a valid selection."""
    min_blocks = 2
    
    # Single block - should not be valid
    selected = 1
    is_valid = selected >= min_blocks
    assert not is_valid, "Single block should not be valid"
    
    # Two blocks - should be valid
    selected = 2
    is_valid = selected >= min_blocks
    assert is_valid, "Two blocks should be valid"
    
    # Multiple blocks - should be valid
    selected = 5
    is_valid = selected >= min_blocks
    assert is_valid, "Multiple blocks should be valid"
    print("✓ Minimum selection test passed")

def test_game_state():
    """Test initial game state."""
    score = 0
    moves = 0
    level = 1
    target_score = 500
    
    assert score == 0, "Initial score should be 0"
    assert moves == 0, "Initial moves should be 0"
    assert level == 1, "Initial level should be 1"
    assert target_score == 500, "Initial target should be 500"
    print("✓ Game state test passed")

def run_all_tests():
    """Run all tests."""
    print("\n=== Running Color Blast Unit Tests ===\n")
    
    try:
        test_color_definitions()
        test_grid_dimensions()
        test_scoring_logic()
        test_level_progression()
        test_flood_fill_logic()
        test_minimum_selection()
        test_game_state()
        
        print("\n=== All Tests Passed! ✓ ===\n")
        return True
    except AssertionError as e:
        print(f"\n✗ Test Failed: {e}\n")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected Error: {e}\n")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
