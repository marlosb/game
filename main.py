from enum import Enum, auto

import pygame

from enemies import Enemy
import map
from settings import screen_properties
from structure import DefensiveStructure

class GameState(Enum):
    STOPPED = auto()
    RUNNING = auto()

class SpawMode(Enum):
    ENEMY = auto()
    STRUCTURE = auto()
    SHOT = auto()

class Game:
    def __init__(self, screen_properties: dict):
        self.screen = pygame.display.set_mode(screen_properties['SCREEN_SIZE'])
        self.TILES_HEIGHT = screen_properties['TILES_HEIGHT'] 
        self.TILES_WIDTH = screen_properties['TILES_WIDTH']
        self.POSITION_OFFSET = 25
        self.FPS = screen_properties['FPS']
        self.clock = pygame.time.Clock()
        self.accumulated_seconds = 0
        self.status = GameState.STOPPED
        self.spaw_mode = SpawMode.STRUCTURE
        self.enemy_list = []
        self.strustures_list = []
        self.enemies_clock = None
        self.level = 1
        self.score = 1000
        self.next_level_score = 5 * self.score

    def initialize(self):
        self.status =  GameState.RUNNING
        pygame.init()
        self.map = map.Map(self, map.init_map, self.TILES_HEIGHT, self.TILES_HEIGHT)      

    def add_timer(self):
        self.accumulated_seconds = self.accumulated_seconds + (self.delta_milliseconds / 1000)
    
    def update(self):
        pygame.display.flip()
        self.delta_milliseconds = self.clock.tick(self.FPS)
        self.add_timer()
        pygame.display.set_caption(f'Great Game Name - FPS: {self.clock.get_fps() : .1f} - Level: {self.level} - Score: {self.score}')
        if self.accumulated_seconds >= 1 and (len(self.enemy_list) < 5):
            self.get_enemy()
            self.accumulated_seconds = 0
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.check_oob() or enemy.check_death():
                self.enemy_list.remove(enemy) 
        for structure in self.strustures_list:
            structure.run()       
    
    def add_score(self, score: int):
        self.score = self.score + score
        if self.score >= self.next_level_score:
            self.up_level()

    def up_level(self):
        self.level = self.level + 1
        self.next_level_score = self.next_level_score * 5

    def get_enemy(self):
        self.enemy_list.append(Enemy(self, self.map.path, 80, 100, 15))

    def get_structure(self):
        pos = pygame.mouse.get_pos()
        pos = (int(pos[0] / self.TILES_WIDTH), int(pos[1] / self.TILES_HEIGHT))
        if pos not in game.map.path:
            self.strustures_list.append(DefensiveStructure(self, position = pos, range = 100))

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for structure in self.strustures_list:
            structure.draw()

    def spaw_object(self):
        spaw_dict = {SpawMode.ENEMY: self.get_enemy,
                     SpawMode.STRUCTURE: self.get_structure}
        spaw_dict[self.spaw_mode]()

    def key_down(self, event):
        if event.key == pygame.K_1:
            self.spaw_mode = SpawMode.STRUCTURE
        elif event.key == pygame.K_2:
            self.spaw_mode = SpawMode.STRUCTURE
        elif event.key == pygame.K_3:
            self.spaw_mode = SpawMode.STRUCTURE

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.KEYDOWN:
                self.key_down(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.spaw_object()

    def run(self):
        if self.status == GameState.STOPPED:
            self.initialize()
        while True:
            self.check_events()
            self.update()
            self.draw()            

    def exit(self):
        self.status == GameState.STOPPED
        pygame.quit()

if __name__ == '__main__':
    game = Game(screen_properties)
    game.run()