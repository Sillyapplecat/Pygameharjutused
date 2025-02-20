import pygame
pygame.init()

screen=pygame.display.set_mode([300,600],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")

pygame.draw.rect(screen, [255, 225, 255], [100, 15, 100, 250], 1)

pygame.draw.circle(screen, [255, 0, 0], [150, 60], 37)
pygame.draw.circle(screen, [255, 255, 0], [150,140], 37)
pygame.draw.circle(screen, [0, 255, 0], [150,220], 37)

pygame.draw.polygon(screen, [0, 0, 225], [[135,500],[130,515],[170,515],[165,500]])
pygame.draw.polygon(screen, [255, 255, 255], [[125,535],[115,550],[185,550],[175,535]])
pygame.draw.polygon(screen, [0, 0, 0], [[125,515],[115,535],[185,535],[175,515]])

pygame.draw.line(screen, [255, 255, 255], [165,265], [165,500], 2)
pygame.draw.line(screen, [255, 255, 255], [135,265], [135,500], 2)
pygame.draw.line(screen, [255, 255, 255], [135,500], [115,550], 2)
pygame.draw.line(screen, [255, 255, 255], [165,500], [185,550], 2)
pygame.draw.line(screen, [255, 255, 255], [115,550], [185,550], 2)


#pygame.draw.polygon(screen, [0, 0, 225], [[135,500],[185,550],[115,550],[165,500]])
pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()