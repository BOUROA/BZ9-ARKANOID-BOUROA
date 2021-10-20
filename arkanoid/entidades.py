import os
import pygame as pg
from pygame.sprite import Sprite

from . import ANCHO, ALTO, FPS


class Raqueta(Sprite):

    velocidad = 5
    margen_inferior = 15
    iteracion = 0
    fps_animacion = 12
    limite_iteracion = FPS/fps_animacion

    def __init__(self):
        super().__init__()
        self.que_imagen_cargar = 0
        self.imagenes = []
        for i in range(3):
            self.imagenes.append(pg.image.load(
                os.path.join('resources', 'images', f'electric0{i}.png'))
            )
        self.image = self.imagenes[self.que_imagen_cargar]
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))

        self.imagenes = []

    def update(self):
        tecla = pg.key.get_pressed()
        if tecla[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

        self.iteracion = self.iteracion + 1
        if self.iteracion == 4:
            self.que_imagen_cargar += 1
            if self.que_imagen_cargar == len(self.imagenes):
                self.que_imagen_cargar = 0
            self.image = self.imagenes[self.que_imagen_cargar]
            self.iteracion = 0


class Ladrillo(Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(os.path.join('resource', 'images', 'greentTile.png')
        self.rect=self.image.get_rect(x=x, y=y)
