import pygame
import math
from math import cos as cos
from math import sin as sin
from pygame.locals import *
from src.color import *
# from src.classes.world import World
from csv import reader

ON_FULLSCREEN = False

FPS = 60

HEIGHT = 1200
WIDTH  = 600

ASP_RATIO = HEIGHT / WIDTH

SIZE_SCREEN = [HEIGHT, WIDTH]

if ON_FULLSCREEN:
    SIZE_SCREEN = [1366, 768]

RUN = True

SCREEN = pygame.display.set_mode(SIZE_SCREEN, pygame.RESIZABLE) 

BG_TEXTURE_SIZE = [100, 100]