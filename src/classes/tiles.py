import src.constantes as const
from src.constantes import *


main_base_A = const.pygame.image.load('src\\assets\\images\\baseA_backgraund.png')
main_base_B = const.pygame.image.load('src\\assets\\images\\baseB_backgraund.png')
main_blank  = const.pygame.image.load('src\\assets\\images\\blank_backgraund.png')
main_wall   = const.pygame.image.load('src\\assets\\images\\wall_backgraund.png' )
        

base_A = const.pygame.transform.scale(main_base_A, [const.BG_TEXTURE_SIZE[0],
                                                    const.BG_TEXTURE_SIZE[1]])
base_B = const.pygame.transform.scale(main_base_B, [const.BG_TEXTURE_SIZE[0],
                                                    const.BG_TEXTURE_SIZE[1]])
blank  = const.pygame.transform.scale(main_blank,  [const.BG_TEXTURE_SIZE[0],
                                                    const.BG_TEXTURE_SIZE[1]])
wall   = const.pygame.transform.scale(main_wall,   [const.BG_TEXTURE_SIZE[0],
                                                    const.BG_TEXTURE_SIZE[1]])

class Fortres(object):
    def __init__(self, base_type, pos_x, pos_y):
        self.pos = [pos_x, pos_y]
        self.life = 100
        self.base_type = base_type

    def scale_tile(self, cam_zoom):
        global base_A
        global base_B
        
        base_A = const.pygame.transform.scale(main_base_A, [const.BG_TEXTURE_SIZE[0] * cam_zoom,
                                                            const.BG_TEXTURE_SIZE[1] * cam_zoom])
        base_B = const.pygame.transform.scale(main_base_B, [const.BG_TEXTURE_SIZE[0] * cam_zoom,
                                                            const.BG_TEXTURE_SIZE[1] * cam_zoom])
    
    def draw_tile(self, pos):
        if self.base_type == 'base a':
            const.SCREEN.blit(base_A, pos)

        if self.base_type == 'base b':
            const.SCREEN.blit(base_B, pos)


class Blank(object):
    def __init__(self, pos_x, pos_y):
        self.base_type = 'blank'
        self.pos = [pos_x, pos_y]

    def scale_tile(self, cam_zoom):
        global blank
                
        blank = const.pygame.transform.scale(main_blank, [const.BG_TEXTURE_SIZE[0] * cam_zoom,
                                                          const.BG_TEXTURE_SIZE[1] * cam_zoom])

    def draw_tile(self, pos):
        const.SCREEN.blit(blank, pos)

class Wall(object):
    def __init__(self, pos_x, pos_y):
        self.base_type = 'wall'
        self.pos = [pos_x, pos_y]

    def scale_tile(self, cam_zoom):
        global wall
                
        wall = const.pygame.transform.scale(main_wall, [const.BG_TEXTURE_SIZE[0] * cam_zoom,
                                                        const.BG_TEXTURE_SIZE[1] * cam_zoom])

    def draw_tile(self, pos):
        const.SCREEN.blit(wall, pos)
