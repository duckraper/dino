import pygame as pg
from sys import exit

if __name__ == '__main__':
    pg.init()

    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        clock.tick(60)
