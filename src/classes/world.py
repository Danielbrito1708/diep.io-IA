import src.constantes as const
from src.constantes import *
from src.classes.player import Player
from src.classes.backgraund import BackGraund

class World(object):
    def __init__(self):
        self.tik = 0
        self.cam_pos = [600, 300]
        self.cam_zoom = 1
        self.game_map = BackGraund()

        self.players = [Player(self.game_map)]

    def scale_world(self, scale):
        self.cam_zoom += scale
        
        if self.cam_zoom < 0.1:
            self.cam_zoom = 0.1
            return
        
        self.game_map.scale_map(self.cam_zoom)
    
    def world_update(self, tik):
        self.tik = tik
        for my_player in self.players:
                my_player.player_update(tik)

    def draw_screen(self):
        self.game_map.draw_map(self.cam_zoom, self.cam_pos)

        for player in self.players:
            player.draw_player(self.cam_zoom, self.cam_pos)
