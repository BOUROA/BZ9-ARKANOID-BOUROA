import pygame as pg

from arkanoid import ALTO, ANCHO
from arkanoid.escenas import HallOfFame, Partida, Portada


class Juego:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption('STARKANOID')
        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            HallOfFame(self.pantalla)]

    def jugar(self):

        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()
