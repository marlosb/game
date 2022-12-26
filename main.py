from enum import Enum, auto

import pygame

from enemies import Enemy
import map
from settings import screen_properties

class GameState(Enum):
    STOPPED = auto()
    RUNNING = auto()

class Game:
    def __init__(self, screen_properties: dict):
        self.screen = pygame.display.set_mode(screen_properties['SCREEN_SIZE'])
        self.TILES_HEIGHT = screen_properties['TILES_HEIGHT'] 
        self.TILES_WIDTH = screen_properties['TILES_WIDTH']
        self.FPS = screen_properties['FPS']
        self.clock = pygame.time.Clock()
        self.status = GameState.STOPPED
        self.enemy_list = []


    def initialize(self):
        self.status =  GameState.RUNNING
        pygame.init()
        self.map = map.Map(self, map.init_map, self.TILES_HEIGHT, self.TILES_HEIGHT)      

    def update(self):
        pygame.display.flip()
        self.delta_milliseconds = self.clock.tick(self.FPS)
        pygame.display.set_caption(f'Great Game Name - FPS: { self.clock.get_fps() : .1f}')
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.check_oob():
                self.enemy_list.remove(enemy)
            

    def get_enemy(self):
        self.enemy_list.append(Enemy(self, self.map.path, 80, 100, 15))

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        for enemy in self.enemy_list:
            enemy.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.get_enemy()

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