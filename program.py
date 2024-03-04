import pygame
from classes.screen_manager import ScreenManager
from classes.sound import Sound


class SoundPlayerApp:
    def __init__(self):
        pygame.init()
        self.screen_manager = ScreenManager(400, 300)
        self.sound = Sound("assets/sounds/intro.mp3")

    def run(self):
        running = True
        
        while running:
            self.screen_manager.screen.fill((0, 0, 0))
            self.screen_manager.draw_button(self.screen_manager.screen_width // 2, self.screen_manager.screen_height // 3, "Play" if self.sound.paused else "Pause", (0, 0, 0))
            self.screen_manager.draw_volume_slider(self.screen_manager.screen_width // 4, 2 * self.screen_manager.screen_height // 3, self.sound.volume)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.is_in_button(event.pos):
                            self.sound.toggle_play_pause()
                        elif self.is_in_slider(event.pos):
                            self.sound.set_volume(event.pos[0] - self.screen_manager.screen_width // 4)
            
            pygame.display.flip()
        
        pygame.quit()
    
    def is_in_button(self, pos):
        return (self.screen_manager.screen_width // 2 - 60 < pos[0] < self.screen_manager.screen_width // 2 + 60 and
                self.screen_manager.screen_height // 3 - 20 < pos[1] < self.screen_manager.screen_height // 3 + 20)
    
    def is_in_slider(self, pos):
        return (self.screen_manager.screen_width // 4 < pos[0] < self.screen_manager.screen_width // 4 + 200 and
                2 * self.screen_manager.screen_height // 3 < pos[1] < 2 * self.screen_manager.screen_height // 3 + 20)

if __name__ == "__main__":
    app = SoundPlayerApp()
    app.run()