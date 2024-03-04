import unittest
from classes.sound import Sound
import os

class TestSound(unittest.TestCase):
    def setUp(self):
        # Initialize Sound object with a sample sound file
        soundPath = os.path.join(os.path.dirname(__file__), "assets/sounds/intro.mp3")
        self.sound = Sound(soundPath)

    def test_initialization(self):
        # Check if Sound object is initialized correctly
        self.assertEqual(self.sound.file_path, "assets/sounds/intro.mp3")
        self.assertTrue(self.sound.paused)
        self.assertEqual(self.sound.volume, 0.5)

    def test_toggle_play_pause(self):
        # Test toggling play/pause functionality
        self.sound.toggle_play_pause()
        self.assertFalse(self.sound.paused)  # Should be playing
        self.sound.toggle_play_pause()
        self.assertTrue(self.sound.paused)  # Should be paused again

    def test_set_volume(self):
        # Test setting volume
        self.sound.set_volume(100)
        self.assertAlmostEqual(self.sound.volume, 0.5)  # Volume should not change (out of bounds)
        self.sound.set_volume(50)
        self.assertAlmostEqual(self.sound.volume, 0.25)  # Volume should be set correctly

if __name__ == "__main__":
    unittest.main()