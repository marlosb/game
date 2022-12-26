from enum import Enum, auto
from math import acos, cos, sin, sqrt

import pygame

class StructureType(Enum):
    RANGE = auto()
    MEELE = auto()

class DefensiveStructure():
    def __init__(self, game, position: tuple[int,int] = (6, 5), type: StructureType = StructureType.RANGE , 
                 rate_of_fire: int = 2, damage: int = 20, range:int = 0):
        self.POSITION_OFFSET = 25
        self.game = game
        self.type = type
        self.rate_of_fire = rate_of_fire
        self.damage = damage
        self.position = (position[0] * self.game.TILES_WIDTH + self.POSITION_OFFSET, 
                         position[1] * self.game.TILES_HEIGHT + self.POSITION_OFFSET)
        self.shots_list = []
        if type == StructureType.RANGE:
            self.range = range
        else:
            self.range = None

    def get_closest_enemy(self):
        closest_enemy = None
        lowest_distance = self.range
        for enemy in self.game.enemy_list:
            distance = sqrt(self.position[0] * enemy.position[0] 
                            + self.position[1] * enemy.position[1])
            if (distance < lowest_distance) and (distance < self.range):
                lowest_distance = distance
                closest_enemy = enemy
        return closest_enemy

    def shot_enemy(self):
        closest_enemy = self.get_closest_enemy()
        if closest_enemy:
            speed = 4 * closest_enemy.speed
            self.shots_list.append(Shot(self.game, self.position, closest_enemy.position, speed))

    def run(self):
        for shot in self.shots_list:
            shot.run()

    def draw(self):
        pygame.draw.circle(self.game.screen, 'blue', self.position, 20)
        for shot in self.shots_list:
            shot.draw()
    
class Shot():
    def __init__(self, game, initial_position: tuple[int, int], final_position: tuple[int, int], speed: int = 100):
        self.game = game
        self.speed = speed
        self.current_position = initial_position
        self.final_position = final_position
        self.current_distance = sqrt(self.current_position[0] * self.final_position[0] 
                                     + self.current_position[1] * self.final_position[1])
        self.angle = acos((self.final_position[0] - self.current_position[0]) / self.current_distance)

    def run(self):
        elapsed_seconds = self.game.delta_milliseconds / 1000
        step = self.speed * elapsed_seconds
        #step = 80 # fix step size for debugging as delta time gets huge on debugging

        self.current_distance = self.current_distance - step

        new_x = self.current_position[0] + self.current_distance * cos(self.angle)
        new_y = self.current_position[1] + self.current_distance * sin(self.angle)
        self.current_position = new_x, new_y

    def draw(self):
        pygame.draw.line(self.game.screen, 'white', self.current_position, self.final_position)
