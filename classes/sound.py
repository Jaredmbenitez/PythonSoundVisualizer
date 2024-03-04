import pygame

class Sound:
    def __init__(self, file_path):
        self.file_path = file_path
        self.paused = True
        self.volume = 0.5
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(self.volume)

    def toggle_play_pause(self):
        if self.paused:
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def set_volume(self, x):
        self.volume = min(max(x / 200, 0), 1)  # Normalize volume value between 0 and 1
        pygame.mixer.music.set_volume(self.volume)