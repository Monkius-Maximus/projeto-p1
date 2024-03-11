from constants import SCREEN_HEIGHT

class Lateral():
    def __init__(self, image_side):
        self.image = image_side
        
    def draw(self, surface):
        surface.blit(self.image, (SCREEN_HEIGHT, 0))