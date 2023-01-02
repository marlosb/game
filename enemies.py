import pygame

class Enemy:
    def __init__(self, game, path, max_life: int = 80, speed: int = 25, size: int = 15, color = 'red'):
        self.game = game
        self.max_life = max_life
        self.speed = speed
        self.path = path
        self.position = ((path[0][0] - 1) * self.game.TILES_WIDTH + self.game.POSITION_OFFSET, 
                         path[0][1] * self.game.TILES_HEIGHT + self.game.POSITION_OFFSET)
        self.path_position = 0
        self.size = size
        self.direction = (1,0)  
        self.color = color
        self.score_value = max_life * speed

    def _get_direction(self, next_x, next_y):
        ''' Method to update the direction enemy is going. 
            Should not be called outsite move method'''
        self.path_position = self.path_position + 1

        delta_x = next_x - self.position[0]
        delta_y = next_y - self.position[1]

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
        ''' Function to move enemy following map path'''
        elapsed_seconds = self.game.delta_milliseconds / 1000
        step = self.speed * elapsed_seconds
        #step = 20 # fix step size for debugging as delta time gets huge on debugging

        next_x = (self.path[self.path_position][0] * self.game.TILES_WIDTH) + self.game.POSITION_OFFSET
        next_y = (self.path[self.path_position][1] * self.game.TILES_HEIGHT) + self.game.POSITION_OFFSET

        updated_x = self.position[0] + (step * self.direction[0])
        updated_y = self.position[1] + (step * self.direction[1])

        if (updated_x > next_x) and (self.direction[0] > 0):
            overrun = next_x - updated_x
            self._get_direction(next_x, next_y)
            updated_x = next_x + (overrun * self.direction[0])
            updated_y = updated_y + (overrun * self.direction[1])
        if (updated_x < next_x) and (self.direction[0] < 0):
            overrun = updated_x - next_x
            self._get_direction(next_x, next_y)
            updated_x = next_x + (overrun * self.direction[0])
            updated_y = updated_y + (overrun * self.direction[1])
        if (updated_y > next_y) and (self.direction[1] > 0):
            overrun = next_y - updated_y
            self._get_direction(next_x, next_y)
            updated_x = updated_x + (overrun * self.direction[0])
            updated_y = next_y + (overrun * self.direction[1])
        if (updated_y < next_y) and (self.direction[1] < 0):
            overrun = updated_y - next_y
            self._get_direction(next_x, next_y)
            updated_x = updated_x + (overrun * self.direction[0])
            updated_y = next_y + (overrun * self.direction[1])

        self.position = updated_x, updated_y

    def update(self):
        self.move()

    def check_oob(self): # check if it is out of boundaries
        max_x, max_y = pygame.display.get_window_size()
        if (self.position[0] + self.size >= max_x + self.size) or (self.position[1]  + self.size >= max_y + self.size):
            self.game.get_capital_damage(self.max_life)
            return True
        return False

    def take_damage(self, damage):
        self.max_life = self.max_life - damage

    def check_death(self):
        if self.max_life > 0:
            return False
        self.game.add_score(self.score_value)
        return True

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, self.position, self.size)