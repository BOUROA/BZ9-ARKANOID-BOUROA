import os
import pygame as pg

from . import ANCHO, ALTO, FPS
from .entidades import Raqueta, Ladrillo


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        tam_letra = 20
        espaciado = 100

        self.pantalla.fill((99, 99, 150))

        self.back = pg.image.load(
            os.path.join('resources', 'images', 'star_wars.jpg')
        )

        self.logo = pg.image.load(
            os.path.join('resources', 'images', 'arkanoid_name.png')
        )
        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', 'Strjmono.ttf'), tam_letra)
        self.texto_inicio = fuente.render(
            'Pulsa  < spacio >  para comenzar', True, 'WHITE')

        self.logo_pos = (ANCHO/2 - self.logo.get_width() /
                         2, 100)
        self.texto_pos = (ANCHO/2 - self.texto_inicio.get_width() /
                          2, ALTO - espaciado - self.texto_inicio.get_height())

        self.pantalla.blit(self.back,(0,0))
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

        self.jugador = Raqueta()
        self.ladrillos = pg.sprite.Group()

    def reset(self):
         num_columnas = 7
         num_filas = 20
         ancho_ladrillo = 90
         alto_ladrillo = 30
         self.ladrillos.empty()
         for fila in range(num_filas):
             for col in range(num_columnas):
                ladrillo = Ladrillo(col*ancho_ladrillo, fila*alto_ladrillo)
                self.ladrillos.add(ladrillo)
       
                
        

    


    def bucle_principal(self):
        self.reset()
        while True:

            self.reloj.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            self.jugador.update()
            self.ladrillos.update()

            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            self.ladrillos.draw(self.pantalla)

            pg.display.flip()


class HallOfFame(Escena):
    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            self.pantalla.fill((99, 150, 99))
            pg.display.flip()
