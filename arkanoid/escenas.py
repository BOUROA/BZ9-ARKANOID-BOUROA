import pygame as pg


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((99, 99, 150))
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
