import pygame

import map
import settings



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = map.Map(self)

    def update(self):
        pygame.display.flip()
        self.clock.tick(settings.FPS)
        pygame.display.set_caption(f'{ self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()