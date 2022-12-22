import pygame

from settings import TILES_WIDTH, TILES_HEIGHT

P = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [P, P, P, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, P, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, P, P, P, P, P, P, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, P, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, P, P, P, P, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, P, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, P, P, P, P, P, P, P, P, P, P, P, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, P, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, P, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, P, 1, ]]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', 
                         (pos[0] * TILES_HEIGHT, pos[1] * TILES_WIDTH, TILES_HEIGHT, TILES_WIDTH), 2)
         for pos in self.world_map]
