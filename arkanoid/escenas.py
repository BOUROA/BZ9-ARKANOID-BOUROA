import os
import pygame as pg
from arkanoid import ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.logo = pg.image.load(
            os.path.join('resources', 'images', 'arkanoid_name.png')
        )

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((99, 99, 150))
            # ANCHO/2 - self.logo.get_width()/2 == (ANCHO-self.logo.get_width())/2
            self.pantalla.blit(
                self.logo, (ANCHO/2 - self.logo.get_width()/2, 100))
            pg.display.flip()


class Partida(Escena):
    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((150, 99, 99))
            pg.display.flip()


class HallOfFame(Escena):
    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((99, 150, 99))
            pg.display.flip()
