import pygame

class ScreenManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sound Player")
        self.font = pygame.font.Font(None, 24)
    
    def draw_button(self, x, y, text, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        pygame.draw.rect(self.screen, (255, 255, 255), (text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20))
        self.screen.blit(text_surface, text_rect)
    
    def draw_volume_slider(self, x, y, volume):
        slider_width = 200
        slider_height = 20
        pygame.draw.rect(self.screen, (150, 150, 150), (x, y, slider_width, slider_height))
        filled_width = int(slider_width * volume)
        pygame.draw.rect(self.screen, (0, 255, 0), (x, y, filled_width, slider_height))