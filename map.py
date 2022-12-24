import pygame

P = False
init_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [P, P, P, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, P, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, P, P, P, P, P, P, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, P, 1, 1, 1, P, P, P, P, 1, ],
    [1, 1, 1, 1, P, P, P, P, 1, 1, 1, P, 1, 1, P, 1, ],
    [1, 1, 1, 1, P, 1, 1, 1, 1, 1, 1, P, 1, 1, P, 1, ],
    [1, 1, 1, 1, P, P, P, P, P, P, P, P, 1, 1, P, 1, ],
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
        self.order_path()

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

    def order_path(self):
        ordered_path = []

        for step, actual_step in enumerate(self.path):
            if step == 0:
                ordered_path.append(actual_step)
                previous_step = actual_step
                continue

            # check if right tile is on path
            candidate_tile = previous_step[0] + 1, previous_step[1]
            if (candidate_tile in self.path) and (candidate_tile not in ordered_path):
                next_step = candidate_tile
            # check if bottom tile is on path
            candidate_tile = previous_step[0], previous_step[1] + 1
            if (candidate_tile in self.path) and (candidate_tile not in ordered_path):
                next_step = candidate_tile
            # check if left tile is on path
            candidate_tile = previous_step[0] - 1, previous_step[1]
            if (candidate_tile in self.path) and (candidate_tile not in ordered_path):
                next_step = candidate_tile
            # check if upp tile is on path
            candidate_tile = previous_step[0], previous_step[1] - 1
            if (candidate_tile in self.path) and (candidate_tile not in ordered_path):
                next_step = candidate_tile
            ordered_path.append(next_step)
            previous_step = next_step         
        self.path = ordered_path

    def get_rectangule(self, position):
        return (position[0] * self.tile_height, 
                position[1] * self.tile_width, 
                self.tile_height, 
                self.tile_width)
    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', 
                         (self.get_rectangule(pos)), 2) for pos in self.world_map]
