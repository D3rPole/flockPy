import pygame
import flock
import quadtree
import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

pygame.init()
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()

w = 800
h = 800
midX = w / 2
midY = h / 2

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("My Game")

f = flock.Flock(700,win)
boids = f.boids

font = pygame.font.SysFont("monospace", 24)

while True:
    dTime = clock.get_time() / 1000.0
    clock.tick(75)

    win.fill((0, 0, 0))


    area = quadtree.rect(midX,midY,w,h)
    tree = quadtree.QuadTree(area,3,10)
    for b in boids:
        tree.addBoid(b)
    tree.drawTree(win, (50,50,50))

    f.update(dTime)

    i = 0
    for b in boids:
        i += 1
        pygame.draw.circle(win,hsv2rgb(i / 700,1,1),(b.position.x,b.position.y),2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    win.blit(fps_text, (10, 10))
    pygame.display.update()