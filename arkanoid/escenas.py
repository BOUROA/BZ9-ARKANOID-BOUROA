import os
import pygame as pg
from pygame import display
from arkanoid import ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.pantalla.fill((99, 99, 150))

        self.logo = pg.image.load(
            os.path.join('resources', 'images', 'arkanoid_name.png')
        )
        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', 'CabinSketch-Bold.ttf'), 20)
        self.texto_inicio = fuente.render(
            'Pulsa <ESPACIO> para comenzar', True, 'white')

        self.logo_pos = (ANCHO/2 - self.logo.get_width() /
                         2, 100)
        self.texto_pos = (ANCHO/2 - self.texto_inicio.get_width() /
                          2, 100 + self.logo.get_height()+20)

        self.pantalla.blit(self.logo, self.logo_pos)
        self.pantalla.blit(self.texto_inicio, self.texto_pos)

        pg.display.flip()

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    # exit() (hace lo mismo)
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return

            # ANCHO/2 - self.logo.get_width()/2 == (ANCHO-self.logo.get_width())/2


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.fondo = pg.image.load(
            os.path.join('resources', 'images', 'background.jpg'))

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((150, 99, 99))

            self.pantalla.blit(self.fondo, (0, 0))
            pg.display.flip()


class HallOfFame(Escena):
    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((99, 150, 99))
            pg.display.flip()
