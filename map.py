import pygame

P = False
init_map = [
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
    def __init__(self, game, init_map , tile_height: int = 600, tile_width: int = 800):
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.game = game
        self.mini_map = init_map
        self.world_map = self.get_map()

    def get_map(self):
        full_map = {}
        self.path = []
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    full_map[(i,j)] = value
                else:
                    self.path.append((i,j))
        return full_map

    def get_rectangule(self, position):
        return (position[0] * self.tile_height, 
                position[1] * self.tile_width, 
                self.tile_height, 
                self.tile_width)
    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', 
                         (self.get_rectangule(pos)), 2) for pos in self.world_map]
