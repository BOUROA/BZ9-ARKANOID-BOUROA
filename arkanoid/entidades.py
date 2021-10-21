import os
from typing import Iterable
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

    def update(self, *args, **kwargs):

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
        if self.iteracion == self.limite_iteracion:
            self.que_imagen_cargar = self.que_imagen_cargar + 1
            if self.que_imagen_cargar == len(self.imagenes):
                self.que_imagen_cargar = 0
            self.image = self.imagenes[self.que_imagen_cargar]
            self.iteracion = 0


class Ladrillo(Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            'resources', 'images', 'greenTile.png'))
        self.rect = self.image.get_rect(x=x, y=y)


class Pelota(Sprite):

    sigo_jugando = True

    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            'resources', 'images', 'ball1.png'))
        self.rect = self.image.get_rect(center=(ANCHO/2, ALTO/2))

        self.velocidad_x = 5
        self.velocidad_y = 5

    def update(self):
        self.rect.x += self.velocidad_x
        if self.rect.right > ANCHO or self.rect.left < 0:
            self.velocidad_x = -self.velocidad_x

        self.rect.y += self.velocidad_y
        if self.rec.top > ALTO:
            self.sigo_jugando = False
            self.reset()
        if self.rect.top <= 0:
            self.velocidad_y = -self.velocidad_y

    def hay_colision(self, otro):
        self.rect.colliderect(otro)
