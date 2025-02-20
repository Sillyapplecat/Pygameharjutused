import pygame
pygame.init()

screen=pygame.display.set_mode([300,300],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")



pygame.draw.circle(screen, [255, 255, 255], [150,65], 30,)
pygame.draw.circle(screen, [255, 255, 255], [150,125], 40,)
pygame.draw.circle(screen, [255, 255, 255], [150,205], 50,)
pygame.draw.circle(screen, [0, 0, 0], [140,65], 5)
pygame.draw.circle(screen, [0, 0, 0], [160,65], 5)

triangle_points = [(155, 75), (150, 90), (145, 75)]
pygame.draw.polygon(screen, [255,102,10], triangle_points)

pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()