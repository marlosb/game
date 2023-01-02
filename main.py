from enum import Enum, auto
from random import randint

import pygame

from enemies import Enemy
from map import Map, init_map
from objects_levels import enemies_properties, structure_properties
from settings import screen_properties
from structure import DefensiveStructure

class GameState(Enum):
    STOPPED = auto()
    RUNNING = auto()

class Game:
    def __init__(self, screen_properties: dict):
        self.screen = pygame.display.set_mode(screen_properties['SCREEN_SIZE'])
        self.TILES_HEIGHT = screen_properties['TILES_HEIGHT'] 
        self.TILES_WIDTH = screen_properties['TILES_WIDTH']
        self.POSITION_OFFSET = 25
        self.FPS = screen_properties['FPS']
        self.status = GameState.STOPPED

    def initialize(self):
        self.status =  GameState.RUNNING
        pygame.init()
        self.map = Map(self, init_map, self.TILES_HEIGHT, self.TILES_HEIGHT)
        self.clock = pygame.time.Clock()
        self.enemy_convoy = EnemyConvoy(self, self.map)
        self.accumulated_seconds = 0
        self.strustures_list = []
        self.level = 1
        self.score = 50000
        self.capital_life = 250
        self.set_next_level_score()
        self.set_max_structures()
    
    def set_next_level_score(self):
        self.next_level_score = 2 * self.score

    def set_max_structures(self):
        self.max_structures = 1 + int(self.level / 2)

    def add_timer(self):
        self.accumulated_seconds = self.accumulated_seconds + (self.delta_milliseconds / 1000)
    
    def update(self):
        pygame.display.flip()
        self.delta_milliseconds = self.clock.tick(self.FPS)
        self.add_timer()
        pygame.display.set_caption(f'Great Game Name - FPS: {self.clock.get_fps() : .1f} - Level: {self.level} - Score: {self.score} - Capital life: {self.capital_life}')
        self.enemy_convoy.update()
        self.update_structure()

    def update_structure(self):
        for structure in self.strustures_list:
            structure.run()

    def add_score(self, score: int):
        self.score = self.score + score
        if self.score >= self.next_level_score:
            self.up_level()

    def get_capital_damage(self, damage: int):
        self.capital_life = self.capital_life - damage

    def up_level(self):
        self.level = self.level + 1
        self.set_next_level_score()
        self.set_max_structures()

    def get_mouse_tile(self):
        pos = pygame.mouse.get_pos()
        return (int(pos[0] / self.TILES_WIDTH), int(pos[1] / self.TILES_HEIGHT))
    
    def get_structure(self):
        pos = self.get_mouse_tile()
        if pos not in game.map.path and len(self.strustures_list) < self.max_structures:
            self.strustures_list.append(DefensiveStructure(self, self.enemy_convoy, position = pos, **structure_properties[self.level]))
            print(f'Structure level is {self.level}  and arguments are {structure_properties[self.level]}')

    def reset_accumulated_timer(self):
        self.accumulated_seconds = 0

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.enemy_convoy.draw()
        self.draw_structures()

    def draw_structures(self):
        for structure in self.strustures_list:
            structure.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.get_structure()

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

class EnemyConvoy:
    def __init__(self, game: Game, map: Map):
        self.game = game
        self.map = map
        self.enemy_list = []
        self.enemies_in_wave = []

    def create_convoy(self):
        min_lengh = max(3, self.game.level - 3)
        max_lengh = min(self.game.level + 3, 10)
        wave_lenght = randint(min_lengh, max_lengh)
        for i in range(0, wave_lenght):
            self.enemies_in_wave.append(randint(1, self.game.level))
    
    def spaw_enemy(self):
        if self.enemies_in_wave and self.game.accumulated_seconds >= 1:
            self.get_enemy(self.enemies_in_wave.pop(0))
            self.game.reset_accumulated_timer()
        if self.game.accumulated_seconds < 5:
            return
        self.create_convoy()

    def get_enemy(self, enemy_level: int):
        self.enemy_list.append(Enemy(self.game, self.map.path, **enemies_properties[enemy_level]))

    def update(self):
        self.spaw_enemy()
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.check_oob() or enemy.check_death():
                self.enemy_list.remove(enemy) 

    def draw(self):
        for enemy in self.enemy_list:
            enemy.draw()

if __name__ == '__main__':
    game = Game(screen_properties)
    game.run()