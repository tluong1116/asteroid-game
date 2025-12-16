import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color='white',
                           center=self.position,
                           radius=self.radius,
                           width=LINE_WIDTH)
        
    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            new_angle = random.uniform(20,50)
            first_asteroid_movement = self.velocity.rotate(new_angle)
            second_asteroid_movement = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid_1.velocity = first_asteroid_movement * 1.2

            asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid_2.velocity = second_asteroid_movement * 1.2


