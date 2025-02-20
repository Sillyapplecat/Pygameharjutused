import pygame
pygame.init()

screen=pygame.display.set_mode([300,300],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")

pygame.draw.rect(screen, [255, 225, 255], [100, 15, 100, 250], 1)

pygame.draw.circle(screen, [255, 0, 0], [150, 60], 37)
pygame.draw.circle(screen, [255, 255, 0], [150,140], 37)
pygame.draw.circle(screen, [0, 255, 0], [150,220], 37)


pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()