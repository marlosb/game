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
        self.direction = (1,0)  

    def get_direction(self):
        current_x = self.position[0]
        current_y = self.position[1]

        self.path_position = self.path_position + 1
        next_x = (self.path[self.path_position][0] * self.game.TILES_WIDTH) + self.POSITION_OFFSET
        next_y = (self.path[self.path_position][1] * self.game.TILES_HEIGHT) + self.POSITION_OFFSET

        delta_x = next_x - current_x
        delta_y = next_y - current_y

        if (abs(delta_x) > abs(delta_y)):
            if delta_x > 0:
                self.direction = (1,0)
            else:
                self.direction = (-1,0)
        else:
            if delta_y > 0:
                self.direction = (0,1)
            else:
                self.direction = (0,-1)

    def move(self):
        elapsed_seconds = self.game.delta_time / 1000
        step = self.speed * elapsed_seconds
        #step = 20

        current_x = self.position[0] + (step * self.direction[0])
        current_y = self.position[1] + (step * self.direction[1])

        next_x = (self.path[self.path_position][0] * self.game.TILES_WIDTH) + self.POSITION_OFFSET
        next_y = (self.path[self.path_position][1] * self.game.TILES_HEIGHT)+ self.POSITION_OFFSET

        if self.direction[0]:
            if current_x > next_x:
                overrun = current_x - next_x
                self.position = next_x, current_y
                self.get_direction()
                overrun_x = overrun * self.direction[0]
                overrun_y = overrun * self.direction[1]
                self.position = next_x + overrun_x, current_y + overrun_y
            else:
                self.position = current_x, current_y
        else:
            if current_y > next_y:
                overrun = current_y - next_y
                self.position = current_x, next_y
                self.get_direction()
                overrun_x = overrun * self.direction[0]
                overrun_y = overrun * self.direction[1]
                self.position = current_x + overrun_x, next_y + overrun_y
            else: 
                self.position = current_x, current_y

    def update(self):
        self.move()

    def check_oob(self): # check if it is out of boundaries
        max_x, max_y = pygame.display.get_window_size()
        if (self.position[0] + self.size >= max_x) or (self.position[1]  + self.size >= max_y):
            return True
        return False

    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', self.position, self.size)

