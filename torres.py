import pygame as pg

class Torre(pg.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)

    def update(self):
        pass
