import pygame
from pygame.sprite import Sprite
from random import randrange

class Alien(Sprite):
  def __init__(self,ai_game):
    super().__init__()
    self.screen = ai_game.screen
    random1 = randrange(4)
    color = 'black'
    if (random1 == 1):
      color = 'blue'
    elif (random1 == 2):
      color = 'green'
    elif (random1 == 3):
      color = 'red'
    self.image = pygame.image.load(f'alien_invasion/images/enemies/enemy{color.title()}{randrange(5) + 1}.png')
    # self.image = pygame.image.load(f'alien_invasion/images/enemies/enemyRed1.png')
    self.rect = self.image.get_rect()
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    self.x = float(self.rect.x)
    self.settings = ai_game.settings

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

  def update(self):
    self.x += self.settings.alien_speed * self.settings.fleet_direction
    self.rect.x = self.x