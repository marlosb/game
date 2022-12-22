from enum import Enum, auto

import pygame

class Enemy:
    def __init__(self, game, path, max_life: int = 80, speed: int = 25, size: int = 15):
        self.game = game
        self.max_life = max_life
        self.speed = speed
        self.path = path
        self.POSITION_OFFSET = 25
        self.position = ((path[0][0] - 1) * self.game.TILES_WIDTH + self.POSITION_OFFSET, 
                         path[0][1] * self.game.TILES_HEIGHT + self.POSITION_OFFSET)
        self.path_position = 0
        self.size = size
           
    def move(self):
        current_x = self.position[0]
        current_y = self.position[1]
        next_x = self.path[self.path_position][0] * self.game.TILES_WIDTH + self.POSITION_OFFSET
        next_y = self.path[self.path_position][1] * self.game.TILES_HEIGHT + self.POSITION_OFFSET

        elapsed_time_seconds = self.game.delta_time / 1000
        step = self.speed * elapsed_time_seconds

        if -0.005 < (next_x - current_x) > 0.005:
            step_x = self.speed * elapsed_time_seconds
            current_x = current_x + step_x

        if -0.005 < (next_y - current_y) > 0.005:
            step_y = self.speed * elapsed_time_seconds
            current_y = current_y + step_y

        if current_x >= next_x and current_y >= next_y:
            self.path_position = self.path_position + 1

        return current_x, current_y

    def update(self):
        self.position = self.move()

    def check_oob(self): # check if it is out of boundaries
        max_x, max_y = pygame.display.get_window_size()
        if (self.position[0] >= max_x) or (self.position[1] >= max_y):
            return True
        return False

    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', self.position, self.size)

