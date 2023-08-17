import src.constantes as const
from src.constantes import *
from src.classes.shot import Shot

def transp(m):
    return list(map(lambda *i: [j for j in i], *m))

class Player(object):
    def __init__(self, game_map):
        self.tik = 0
        self.pos = [0, 0]
        self.ang = 0
        self.life = 1
        self.direction = [0, 0]
        self.shot_reload = self.tik
        self.shots = []
        self.vel = 0
        self.radios = 8

    def player_input(self, direction=0, vel=0.2, shot=False):
        self.player_move(direction, vel)

        if shot == True:
            self.shot()

    def on_colision(self):
        pass

    def player_move(self, ang, vel):
        self.ang += ang
        self.pos[0] += cos(math.radians(self.ang)) * vel
        self.pos[1] += sin(math.radians(self.ang)) * vel

    def player_update(self, tik):
        self.tik = tik
        for shot in self.shots:
            shot.shot_update()

    def shot(self):
        if (self.tik - self.shot_reload) > 5:
            pos_x = self.pos[0]
            pos_y = self.pos[1]
            ang = self.ang

            new_shot = Shot([pos_x, pos_y], ang)

            self.shots.append(new_shot)
            self.shot_reload = self.tik

    def draw_player(self, zoom, cam_pos):
        b_pos = [self.pos[0] * zoom + cam_pos[0], self.pos[1] * zoom + cam_pos[1]]
        radiano = const.math.radians(self.ang)

        z_cos = cos(radiano) * zoom
        z_sin = sin(radiano) * zoom

        points = [[((z_cos * 0 ) - (z_sin *  20)) + b_pos[0], ((z_sin * 0 ) + (z_cos *  20)) + b_pos[1]],
                  [((z_cos * 60) - (z_sin *  20)) + b_pos[0], ((z_sin * 60) + (z_cos *  20)) + b_pos[1]],
                  [((z_cos * 60) - (z_sin * -20)) + b_pos[0], ((z_sin * 60) + (z_cos * -20)) + b_pos[1]],
                  [((z_cos * 0 ) - (z_sin * -20)) + b_pos[0], ((z_sin * 0 ) + (z_cos * -20)) + b_pos[1]]]

        for shot in self.shots:
            shot.draw_shot(zoom, cam_pos)
        
        const.pygame.draw.polygon(const.SCREEN, const.WHITE(50), points)                                               
        const.pygame.draw.polygon(const.SCREEN, const.WHITE(25), points, int(self.radios * zoom))
                                                                  
        const.pygame.draw.circle(const.SCREEN, const.BLUE(b=200), [b_pos[0], b_pos[1]], 30 * zoom)
        const.pygame.draw.circle(const.SCREEN, const.BLUE(b=100), [b_pos[0], b_pos[1]], 30 * zoom, int(8 * zoom))
        
        