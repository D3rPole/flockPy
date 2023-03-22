import boid
import pygame.math as m
class Flock:
    flockSize = 0

    target = m.Vector2(400,300)
    targetFactor = 1
    cohesionFactor = 1
    seperationFactor = 1
    alignmentFactor = 1

    boids = []

    def __init__(self, flockSize, win):
        self.target = m.Vector2(win.get_width() / 2, win.get_height() / 2)
        self.win = win
        self.flockSize = flockSize
        self.initBoids()

    def initBoids(self):
        for i in range(self.flockSize):
            self.boids.append(boid.Boid(self.win))

    def update(self,dtime):
        for b in self.boids:

            targetForce = (self.target - b.position)

            netForce = targetForce * self.targetFactor

            b.update(dtime)
            b.applyForce(netForce,dtime)

