import pygame

class Img:
  def __init__(self):
    self.x = 0
    self.y = 0
  def put_img(self, address):
    if address[-3:] == "png":
      self.img = pygame.image.load(address).convert_alpha()
    else:
      self.img = pygame.image.load(address)
  def change_img(self, sx ,sy):
    self.img = pygame.transform.scale(self.img, (sx, sy))
    self.sx, self.sy = self.img.get_size()
  def show(self, screen):
    screen.blit(self.img, (self.x, self.y))
