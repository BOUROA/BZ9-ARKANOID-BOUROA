# Version Arkanoid Raul

from arkanoid import ANCHO, ALTO
from arkanoid.game import Juego

if __name__ == '__main__':
    print("main: main.py")
    print(f'Estoy jugando a {ANCHO}x{ALTO}')
    juego = Juego()
    juego.jugar()
