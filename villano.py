import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/Mina.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		self.dir = "b"
		self.velocidad=vel
        
	def update(self):
		if self.dir == "b":
			self.rect.y += self.velocidad
		(""")elif self.dir == "b":
			self.rect.y -= self.velocidad
		if self.rect.y>=0:
			self.dir="b"(""")
		if self.rect.y<=608:
			self.dir="b"
