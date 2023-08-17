import src.constantes as const
from src.constantes import *
from src.classes.tiles import Fortres, Blank, Wall

def transp(m):
    return list(map(lambda *i: [j for j in i], *m))

class BackGraund(object):
    def __init__(self):
        self.tile_map = self.load_map('src\\assets\\maps\\map_2.0.csv')
        self.inverted_tile_map = transp(self.tile_map)
        print(self.tile_map)

    def load_map(self, arquivo):
        with open(arquivo, 'r') as csv_file:
            csv_reader = const.reader(csv_file)
            list_of_rows = list(csv_reader)
            
        index_i = 0
        pos_i = int(-len(list_of_rows) / 2)
        for i in list_of_rows:
            index_j = 0
            pos_j = int(-len(list_of_rows[0]) / 2)

            for j in i:
                pos_x = pos_i * const.BG_TEXTURE_SIZE[0]
                pos_y = pos_j * const.BG_TEXTURE_SIZE[1]

                if j == 'base a':
                    list_of_rows[index_i][index_j] = Fortres('base a', pos_x, pos_y)
                if j == 'base b':
                    list_of_rows[index_i][index_j] = Fortres('base b', pos_x, pos_y)
                if j == 'blank':
                    list_of_rows[index_i][index_j] = Blank(pos_x, pos_y)
                if j == 'wall':
                    list_of_rows[index_i][index_j] = Wall(pos_x, pos_y)
                
                index_j += 1
                pos_j += 1
                
            index_i += 1
            pos_i += 1

        return list_of_rows

    def scale_map(self, cam_zoom):
        for i in self.tile_map:
            for j in i:
                j.scale_tile(cam_zoom)

    def draw_map(self, cam_zoom, cam_pos):
        index_line = -len(self.tile_map) / 2

        for line in self.tile_map:
            index_coluna = -len(self.tile_map[0]) / 2

            for element in line:
                pos_x = element.pos[0] * cam_zoom + cam_pos[0]
                pos_y = element.pos[1] * cam_zoom + cam_pos[1]

                element.draw_tile([pos_x, pos_y])

                index_coluna += 1
            index_line += 1
