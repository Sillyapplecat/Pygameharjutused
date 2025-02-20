import pygame
pygame.init()

screen=pygame.display.set_mode([300,300],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")




screen.fill([204, 255, 255])

pygame.draw.ellipse(screen, [255, 255, 255], [30, 30, 40, 20])
pygame.draw.ellipse(screen, [255, 255, 255], [30, 40, 60, 40])
pygame.draw.ellipse(screen, [255, 255, 255], [10, 40, 40, 30])

pygame.draw.ellipse(screen, [255, 255, 255], [90, 90, 40, 20])
pygame.draw.ellipse(screen, [255, 255, 255], [90, 100, 60, 40])
pygame.draw.ellipse(screen, [255, 255, 255], [70, 100, 40, 30])

pygame.draw.ellipse(screen, [255, 255, 255], [230, 90, 40, 20])
pygame.draw.ellipse(screen, [255, 255, 255], [230, 100, 60, 40])
pygame.draw.ellipse(screen, [255, 255, 255], [210, 100, 40, 30])

pygame.draw.circle(screen, [255, 255, 0], [0,0], 45)
pygame.draw.line(screen, [255, 255, 0], [0,0], [0, 60], 10)
pygame.draw.line(screen, [255, 255, 0], [0,0], [20, 50], 10)
pygame.draw.line(screen, [255, 255, 0], [0,0], [40, 40], 10)
pygame.draw.line(screen, [255, 255, 0], [0,0], [60, 20], 10)
pygame.draw.line(screen, [255, 255, 0], [0,0], [70, 0], 10)
pygame.draw.line(screen, [255, 255, 0], [0,0], [0, 0], 10)
pygame.draw.circle(screen, [255, 255, 255], [150,65], 30,)
pygame.draw.circle(screen, [255, 255, 255], [150,125], 40,)
pygame.draw.circle(screen, [255, 255, 255], [150,205], 50,)
pygame.draw.circle(screen, [0, 0, 0], [140,65], 5) #silm
pygame.draw.circle(screen, [0, 0, 0], [160,65], 5) #silm
pygame.draw.circle(screen, [0, 0, 0], [150,100], 5) #nööp
pygame.draw.circle(screen, [0, 0, 0], [150,125], 5) #nööp
pygame.draw.circle(screen, [0, 0, 0], [150,150], 5) #nööp
pygame.draw.line(screen, [0, 0, 0], [120,100], [65,150], 2) #käsi
pygame.draw.line(screen, [0, 0, 0], [180,100], [235,150], 2) #käsi
pygame.draw.rect(screen, [0, 0, 0], [110, 40, 80, 10])
pygame.draw.rect(screen, [0, 0, 0], [125, 10, 50, 40])
pygame.draw.line(screen, [0, 0, 0], [65,100], [65,230], 2)

#hari
pygame.draw.line(screen, [0, 0, 0], [65,230], [45,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [50,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [55,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [60,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [65,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [70,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [75,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [80,290], 2)
pygame.draw.line(screen, [0, 0, 0], [65,230], [85,290], 2)

triangle_points = [(155, 75), (150, 90), (145, 75)]
pygame.draw.polygon(screen, [255,102,10], triangle_points)

pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()