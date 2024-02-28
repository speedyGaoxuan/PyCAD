# 基于pygame的图形化CAD编辑器
# made by Gaoxuan

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

mainwindow = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('PyCAD')
# icon = pygame.image.load('./img/icon.png')
# pygame.display.set_icon(icon)

WHITE = (255, 255, 255)


def display_main_window():
    mainwindow.fill(WHITE)


while True:
    display_main_window()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(60)
