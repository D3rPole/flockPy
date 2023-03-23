import boid
import pygame.math as m
class Flock:
    flockSize = 0

    target = m.Vector2(400,300)
    targetFactor = 0
    cohesionFactor = 0
    seperationFactor = 10
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
            cohesionForce = m.Vector2()
            seperationForce = m.Vector2()
            if(hasattr(b,"quad")):
                boidInRange = b.quad.parent.getBoids()
                avrgPos = m.Vector2()
                for bb in boidInRange:
                    if(bb != b):
                        seperationForce += (b.position - bb.position) / b.position.distance_squared_to(bb.position)
                        avrgPos += bb.position
                
                avrgPos = avrgPos / len(boidInRange)

                cohesionForce = (avrgPos - b.position)

            targetForce = (self.target - b.position)

            netForce = targetForce * self.targetFactor + cohesionForce * self.cohesionFactor + seperationForce * self.seperationFactor

            b.update(dtime)
            b.applyForce(netForce,dtime)

