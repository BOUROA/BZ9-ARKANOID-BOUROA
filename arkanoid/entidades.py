import os
import pygame as pg
from pygame.sprite import Sprite

from . import ANCHO, ALTO


class Raqueta(Sprite):
    velocidad = 5
    margen_inferior = 15

    def __init__(self):
        super().__init__()
        self.image = pg.image.load(
            os.path.join('resources', 'images', 'electric00.png')
        )

        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))

    def update(self):
        tecla = pg.key.get_pressed()
        if tecla[pg.K_RIGHT]:
            self.rect.x += self.velocidad
        if tecla[pg.K_LEFT]:
            self.rect.x -= self.velocidad
