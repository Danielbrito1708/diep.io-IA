import src.constantes as const
from src.constantes import *

class Shot(object):
    def __init__(self, s_pos, direc):
        self.s_pos = s_pos
        self.s_dir = direc
        self.s_vel = 20

    def shot_update(self):
        self.s_pos[0] += cos(math.radians(self.s_dir)) * self.s_vel
        self.s_pos[1] += sin(math.radians(self.s_dir)) * self.s_vel

    def on_colision(self):
        pass
    def draw_shot(self, zoom, cam_pos):
        pos = [self.s_pos[0] * zoom + cam_pos[0], self.s_pos[1] * zoom + cam_pos[1]]

        const.pygame.draw.circle(const.SCREEN, const.GREEN(c=90), [pos[0], pos[1]], 15 * zoom)
        const.pygame.draw.circle(const.SCREEN, const.GREEN(c=50), [pos[0], pos[1]], 15 * zoom, int(8 * zoom))