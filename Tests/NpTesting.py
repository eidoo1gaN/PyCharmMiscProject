import numpy as np
import pygame as pg
x = np.array([6, 7])
y = [6, 7]

pg.init()

running = True
screen = pg.display.set_mode((1280, 720))
screen.fill((2, 2, 100))
circle = pg.draw.circle(screen, (2, 239, 238), (400, 400), 100)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()