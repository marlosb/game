from enum import Enum, auto
from math import acos, cos, sin, sqrt

import pygame

class StructureType(Enum):
    RANGE = auto()
    MEELE = auto()

class DefensiveStructure():
    def __init__(self, game, enemies, position: tuple[int,int] = (6, 5), type: StructureType = StructureType.RANGE , 
                 rate_of_fire: int = 2, damage: int = 20, range: int = 0, color : str = 'blue'):
        self.game = game
        self.enemies = enemies
        self.type = type
        self.seconds_between_shots = 1 / rate_of_fire 
        self.damage = damage
        self.position = (position[0] * self.game.TILES_WIDTH + self.game.POSITION_OFFSET, 
                         position[1] * self.game.TILES_HEIGHT + self.game.POSITION_OFFSET)
        self.color = color
        self.clock = None
        self.delta_milliseconds = 0
        self.accumulated_seconds = 0
        self.shot = None
        if type == StructureType.RANGE:
            self.range = range
        else:
            self.range = None

    def add_timer(self):
        self.accumulated_seconds = self.accumulated_seconds + (self.delta_milliseconds / 1000)

    def ready_to_shot(self):
        if not self.clock:
            self.clock = pygame.time.Clock()
            return True
        else:
            self.clock.tick()
            self.delta_milliseconds = self.clock.get_time()
            self.add_timer()
            if self.accumulated_seconds >= self.seconds_between_shots:
                return True
        return False

    def get_closest_enemy(self):
        closest_enemy = False
        lowest_distance = self.range
        for enemy in self.enemies.enemy_list:
            distance = sqrt((self.position[0] - enemy.position[0]) ** 2 
                            + (self.position[1] - enemy.position[1]) ** 2)
            if (distance < lowest_distance) and (distance < self.range):
                lowest_distance = distance
                closest_enemy = enemy
        return closest_enemy

    def shot_enemy(self):
        if not self.ready_to_shot():
            return
        closest_enemy = self.get_closest_enemy()
        if closest_enemy:
            self.shot_seconds = self.accumulated_seconds
            self.accumulated_seconds = 0
            self.shot = closest_enemy
            closest_enemy.take_damage(self.damage)

    def run(self):
        self.shot_enemy()
    
    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, self.position, 20)
        if self.shot and (self.accumulated_seconds <= 0.15):
            pygame.draw.line(self.game.screen, 'white', self.position, self.shot.position, width=3)