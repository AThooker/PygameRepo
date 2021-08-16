import pygame

from models import Spaceship, Meteor
from utils import get_random_position, load_sprite

class SpaceRocks:
    MIN_METEOR_DISTANCE = 250

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("space2", False)
        self.clock = pygame.time.Clock()
        self.meteor = []
        self.lasers = []
        self.spaceship = Spaceship((400,300), self.lasers.append)

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if(
                    position.distance_to(self.spaceship.position) > self.MIN_METEOR_DISTANCE
                ):
                    break
            self.meteor.append(Meteor(position))

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
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                quit()
            elif(
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for meteor in self.meteor:
                if meteor.collides_with(self.spaceship): 
                    self.spaceship = None
                    break

        for bullet in self.lasers[:]:
            for meteor in self.meteor[:]:
                if meteor.collides_with(bullet):
                    self.meteor.remove(meteor)
                    self.lasers.remove(bullet)
                    break

    def _draw(self):
        self.screen.blit(self.background,(0,0))
        
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def _get_game_objects(self):
        game_objects = [*self.meteor, *self.lasers]

        if self.spaceship:
            game_objects.append(self.spaceship)
        
        return game_objects