import pygame
pygame.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("Harjutamine")



pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()