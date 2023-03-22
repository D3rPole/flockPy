import random
import pygame.math as m
class Boid:
    def __init__(self, win) -> None:
        self.w = win.get_width()
        self.h = win.get_height()
        self.position = m.Vector2(self.w/4 + random.random() * self.w/2, self.h/4 + random.random() * self.h/2)
        self.velocity = m.Vector2(0,0)
    
    def setQuad(self, quad):
        self.quad = quad

    def update(self, dtime):
        self.position += self.velocity * dtime

        if(self.position.y < 0):
            self.position.y += self.h
            self.velocity.y = -abs(self.velocity.y)

        if(self.position.y > self.h):
            self.position.y -= self.h
            self.velocity.y = abs(self.velocity.y)

        if(self.position.x < 0):
            self.position.x += self.w
            self.velocity.x = -abs(self.velocity.x)

        if(self.position.x > self.w):
            self.position.x -= self.w
            self.velocity.x = abs(self.velocity.x)

    def applyForce(self, force, dtime):
        self.velocity += force * dtime