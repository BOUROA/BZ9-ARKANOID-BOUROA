import pygame as pg

from arkanoid import ALTO, ANCHO


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        """Este el el bucle principal."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.pantalla.fill((99, 99, 99))
            pg.display.flip()


if __name__ == '__main__':
    print("main: game.py")
    Arkanoid()
