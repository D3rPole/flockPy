import pygame
import math
class rect:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def inRect(self,x,y):
        return x > self.x - self.w / 2 and x < self.x + self.w / 2 and y > self.y - self.h / 2 and y < self.y + self.h / 2
        

class QuadTree:
    def __init__(self, area, capacity, maxDepth):
        self.maxDepth = maxDepth
        self.depth = 0
        self.area = area
        self.capacity = capacity
        self.boids = []
        self.divided = False

    def setParentTree(self, parent):
        self.parent = parent
        self.depth = parent.depth + 1
    
    def addBoid(self, boid):
        if(not self.area.inRect(boid.position.x,boid.position.y)):
           return
        
        if(not self.divided):
            if(len(self.boids) < self.capacity or self.depth >= self.maxDepth):
                self.boids.append(boid)
            else:
                self.divide()
        else:
            self.nw.addBoid(boid)
            self.ne.addBoid(boid)
            self.sw.addBoid(boid)
            self.se.addBoid(boid)


    def divide(self):
        self.divided = True
        nw = rect(self.area.x - self.area.w / 4,self.area.y - self.area.h / 4, self.area.w/2, self.area.h/2)
        self.nw = QuadTree(nw,self.capacity, self.maxDepth)
        ne = rect(self.area.x + self.area.w / 4,self.area.y - self.area.h / 4, self.area.w/2, self.area.h/2)
        self.ne = QuadTree(ne,self.capacity, self.maxDepth)
        sw = rect(self.area.x - self.area.w / 4,self.area.y + self.area.h / 4, self.area.w/2, self.area.h/2)
        self.sw = QuadTree(sw,self.capacity, self.maxDepth)
        se = rect(self.area.x + self.area.w / 4,self.area.y + self.area.h / 4, self.area.w/2, self.area.h/2)
        self.se = QuadTree(se,self.capacity, self.maxDepth)

        self.nw.setParentTree(self)
        self.ne.setParentTree(self)
        self.sw.setParentTree(self)
        self.se.setParentTree(self)

        for _boid in self.boids:
            self.nw.addBoid(_boid)
            self.ne.addBoid(_boid)
            self.sw.addBoid(_boid)
            self.se.addBoid(_boid)
        
        del(self.boids)


    def drawTree(self, window):
        if(self.divided):
            self.nw.drawTree(window)
            self.ne.drawTree(window)
            self.sw.drawTree(window)
            self.se.drawTree(window)
        else:
            rect = pygame.Rect(math.ceil(self.area.x - self.area.w / 2)
                               , math.ceil(self.area.y - self.area.h / 2)
                               , math.ceil(self.area.w)
                               , math.ceil(self.area.h))
            pygame.draw.rect(window,(100,255,100),rect,1)
