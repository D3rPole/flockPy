import boid
import pygame.math as m
class Flock:
    flockSize = 0

    target = m.Vector2(400,300)
    targetFactor = 0
    cohesionFactor = 2
    seperationFactor = 5000
    alignmentFactor = 10

    viewDistance = 50

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
            alignmentForce = m.Vector2()
            f = m.Vector2()
            if(hasattr(b,"quad")):
                boidInRange = b.quad.getBoidsInRadius(b.position.x,b.position.y,self.viewDistance)
                avrgPos = m.Vector2()
                i = 0
                for bb in boidInRange:
                    if(bb != b):
                        if(bb.position.distance_to(b.position) < self.viewDistance):
                            i = i + 1
                            seperationForce += (b.position - bb.position) / b.position.distance_squared_to(bb.position)
                            alignmentForce += bb.velocity
                            avrgPos += bb.position
                
                if(self.target.distance_to(b.position) < 200000):
                    f = (b.position - self.target) / self.target.distance_squared_to(b.position)
                if(i > 0):
                    avrgPos = avrgPos / i
                    cohesionForce = (avrgPos - b.position)
                    alignmentForce = alignmentForce / (len(boidInRange) - 1)

            targetForce = (self.target - b.position)
            netForce = f * 10000 + targetForce * self.targetFactor + cohesionForce * self.cohesionFactor + seperationForce * self.seperationFactor + alignmentForce * self.alignmentFactor
            b.update(dtime)
            b.applyForce(netForce,dtime)

