from enum import Enum, auto

import pygame

import map
from settings import ScreenProperties, screen_properties

class GameState(Enum):
    STOPPED = auto()
    RUNNING = auto()

class Game:
    def __init__(self, screen_properties: ScreenProperties):
        self.screen = pygame.display.set_mode(screen_properties.SCREEN_SIZE)
        self.TILES_HEIGHT = screen_properties.TILES_HEIGHT
        self.TILES_WIDTH = screen_properties.TILES_WIDTH
        self.FPS = screen_properties.FPS
        self.clock = pygame.time.Clock()
        self.status: GameState = GameState.STOPPED

    def initialize(self):
        self.status: GameState = GameState.RUNNING
        pygame.init()
        self.new_game()

    def new_game(self):
        self.map = map.Map(self, self.TILES_HEIGHT, self.TILES_HEIGHT)

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)
        pygame.display.set_caption(f'Great Game Name - FPS: { self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

    def check_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

    def run(self):
        if self.status == GameState.STOPPED:
            self.initialize()
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game(screen_properties)
    game.run()