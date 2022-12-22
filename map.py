import pygame

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
    def __init__(self, game, tile_height: int = 600, tile_width: int = 800):
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    @staticmethod
    def get_rectangule(position, height, width):
        return (position[0] * height, position[1] * width, height, width)
    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', 
                         (self.get_rectangule(pos, self.tile_height, self.tile_width)), 2)
         for pos in self.world_map]
