import pygame
import flock
import quadtree

pygame.init()
clock = pygame.time.Clock()

w = 600
h = 600
midX = w / 2
midY = h / 2

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("My Game")

f = flock.Flock(1000,win)
boids = f.boids

font = pygame.font.SysFont("monospace", 24)

while True:
    dTime = clock.get_time() / 1000.0
    clock.tick(1000)

    win.fill((0, 0, 0))

    area = quadtree.rect(midX,midY,w,h)
    tree = quadtree.QuadTree(area,5,100)
    for b in boids:
        tree.addBoid(b)

    f.update(dTime)

    for b in boids:
        pygame.draw.circle(win,(255,0,0),(b.position.x,b.position.y),2)

    #tree.drawTree(win, (255,100,100))
    #boids[0].quad.parent.drawTree(win, (0,255,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    win.blit(fps_text, (10, 10))
    pygame.display.update()