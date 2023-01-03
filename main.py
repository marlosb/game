from enum import Enum, auto

import pygame

from enemies import EnemyConvoy
from map import Map, init_map
from settings import screen_properties
from structure import DefensiveStructuresNetwork

class GameState(Enum):
    STOPPED = auto()
    PAUSED = auto()
    RUNNING = auto()
    GAME_OVER = auto()

class Game:
    def __init__(self, screen_properties: dict):
        self.screen = pygame.display.set_mode(screen_properties['SCREEN_SIZE'])
        self.TILES_HEIGHT = screen_properties['TILES_HEIGHT'] 
        self.TILES_WIDTH = screen_properties['TILES_WIDTH']
        self.POSITION_OFFSET = 25
        self.FPS = screen_properties['FPS']
        self.status = GameState.STOPPED

    def initialize(self):
        self.status =  GameState.PAUSED
        pygame.init()
        self.map = Map(self, init_map, self.TILES_HEIGHT, self.TILES_HEIGHT)
        self.clock = pygame.time.Clock()
        self.accumulated_seconds = 0
        self.level = 1
        self.score = 50000
        self.capital_initial_life = self.capital_life = 250
        self.set_next_level_score()
        self.enemy_convoy = EnemyConvoy(self, self.map)
        self.defense = DefensiveStructuresNetwork(self, self.map, self.enemy_convoy)
    
    def set_next_level_score(self):
        self.next_level_score = 1.6 * self.score

    def add_timer(self):
        self.accumulated_seconds = self.accumulated_seconds + (self.delta_milliseconds / 1000)
    
    def update(self):
        self.delta_milliseconds = self.clock.tick(self.FPS)
        self.add_timer()
        pygame.display.set_caption(f'Great Game Name - Level: {self.level} - Score: {self.score} - Capital life: {self.capital_porcentage_life()}%')
        self.enemy_convoy.update()
        self.defense.update()
        pygame.display.flip()

    def add_score(self, score: int):
        self.score = self.score + score
        if self.score >= self.next_level_score:
            self.up_level()

    def game_over(self):
        self.status = GameState.PAUSED
        self.level = 0
    
    def get_capital_damage(self, damage: int):
        self.capital_life = self.capital_life - damage
        if self.capital_life <= 0:
            self.game_over()

    def recovery_capital(self, recovery_fraction: float):
        self.capital_life = int(self.capital_life * (1 + recovery_fraction))
        if self.capital_life > self.capital_initial_life:
            self.capital_life = self.capital_initial_life

    def capital_porcentage_life(self):
        return int(100 * (self.capital_life / self.capital_initial_life))

    def up_level(self):
        self.level = self.level + 1
        if self.level == 10:
            self.status = GameState.PAUSED
        self.set_next_level_score()
        self.defense.set_max_structures()
        if self.level == 5:
            self.recovery_capital(0.1) # recovers 10% of capital live each level up
        self.status = GameState.PAUSED
    
    def get_mouse_tile(self):
        pos = pygame.mouse.get_pos()
        return (int(pos[0] / self.TILES_WIDTH), int(pos[1] / self.TILES_HEIGHT))

    def reset_accumulated_timer(self):
        self.accumulated_seconds = 0

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.enemy_convoy.draw()
        self.defense.draw()

    def mouse_clicked(self):
        if self.status == GameState.RUNNING:
            self.defense.get_structure()
        elif 0 < self.level < 10:
            self.status = GameState.RUNNING
            self.reset_accumulated_timer()
            self.clock.tick(self.FPS)
        else:
            self.exit()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicked()

    def display_message(self):
        image = pygame.image.load(f'images/image{self.level}.png')
        self.screen.blit(image, (168, 65))
        pygame.display.flip()
        self.check_events()

    def _run(self):
        self.check_events()
        self.update()
        self.draw()  

    def run(self):
        run_modes_dict = {GameState.STOPPED: self.initialize,
                          GameState.PAUSED: self.display_message,
                          GameState.RUNNING: self._run}
        run_modes_dict[self.status]()

    def exit(self):
        self.status == GameState.GAME_OVER
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = Game(screen_properties)
    while True:
        game.run()