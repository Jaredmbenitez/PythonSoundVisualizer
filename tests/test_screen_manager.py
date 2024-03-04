import unittest
import pygame
from unittest.mock import MagicMock
from classes.screen_manager import ScreenManager

class TestScreenManager(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen_manager = ScreenManager(400, 300)

    def test_draw_button(self):
        """Test the draw_button method."""
        self.screen_manager.screen.fill((0, 0, 0))  # Clear the screen
        self.screen_manager.draw_button(200, 100, "Test", (255, 255, 255))
        # Assuming button is drawn at (200, 100) with text "Test"
        pixel_color = self.screen_manager.screen.get_at((200, 100))
        self.assertEqual(pixel_color, (255, 255, 255, 255), "Button color is not white.")

    def test_draw_volume_slider(self):
        """Test the draw_volume_slider method."""
        self.screen_manager.screen.fill((0, 0, 0))  # Clear the screen
        self.screen_manager.draw_volume_slider(100, 200, 0.5)
        # Assuming slider is drawn at (100, 200) with volume 0.5
        pixel_color = self.screen_manager.screen.get_at((150, 210))
        self.assertEqual(pixel_color, (0, 255, 0, 255), "Slider color is not green.")

if __name__ == "__main__":
    unittest.main()
