# 基于pygame的图形化CAD编辑器
# made by Gaoxuan

import pygame, sys, time
from pygame.locals import *

mainwindow = pygame.display.set_mode((1600, 900), pygame.RESIZABLE, 32)
pygame.display.set_caption('PyCAD')
# icon = pygame.image.load('./img/icon.png')
# pygame.display.set_icon(icon)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (225, 225, 0)

pygame.init()
fpsClock = pygame.time.Clock()

bar_font_file = pygame.font.match_font('SimHei')
bar_font = pygame.font.Font(bar_font_file, 20)

menu_bar_tabs = ['文件', '编辑']
tab_interval = 10


def display_menu_bar_tabs():
    tabx = tab_interval
    for tab_text in menu_bar_tabs:
        tab_text_surface = bar_font.render(tab_text, True, BLACK, GREEN)
        tab_rect = tab_text_surface.get_rect()
        tab_rect.topleft = (tabx, 8)
        tabx = tabx + tab_rect.width + tab_interval
        mainwindow.blit(tab_text_surface, tab_rect)


def display_menu_bar():
    menu_bar_rect = (0, 0, mainwindow_w, 36)
    pygame.draw.rect(mainwindow, BLUE, menu_bar_rect)
    display_menu_bar_tabs()


def display_xy_status():
    xy_status = 'x:%d y:%d' % (mouse_x, mouse_y)
    tab_text_surface = bar_font.render(xy_status, True, BLACK, YELLOW)
    tab_rect = tab_text_surface.get_rect()
    tab_rect.topleft = (10, mainwindow_h - 28)
    mainwindow.blit(tab_text_surface, tab_rect)


def display_status_bar():
    status_bar_rect = (0, mainwindow_h - 36, mainwindow_w, 36)
    pygame.draw.rect(mainwindow, RED, status_bar_rect)
    display_xy_status()


def display_main_window():
    mainwindow.fill(WHITE)
    display_menu_bar()
    display_status_bar()


while True:
    mainwindow_w, mainwindow_h = pygame.display.get_surface().get_size()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    display_main_window()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(60)
