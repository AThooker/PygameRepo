import pygame

from models import GameObject
from utils import load_sprite

class SpaceRocks:

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("space2", False)
        self.clock = pygame.time.Clock()
        self.spaceship = GameObject(
            (400, 300), load_sprite("spaceship"), (0,0)
        )
        self.meteor = GameObject(
            (400, 300), load_sprite("meteor"), (1,0)
        )

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Pew Pew")

    def _handle_input(self):
        for event in pygame.event.get():
            # \ tells the program the line of code continues on the next line (from 22-23)
            if event.type == pygame.QUIT or( \
            event.type == pygame.KEYDOWN and \
                event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        self.spaceship.move()
        self.meteor.move()

    def _draw(self):
        self.screen.blit(self.background,(0,0))
        self.spaceship.draw(self.screen)
        self.meteor.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)