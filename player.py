from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = pl_pos
        self.angle = pl_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += pl_speed * cos_a
            self.y += pl_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -pl_speed * cos_a
            self.y += -pl_speed * sin_a
        if keys[pygame.K_a]:
            self.x += pl_speed * sin_a
            self.y += -pl_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -pl_speed * sin_a
            self.y += pl_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
