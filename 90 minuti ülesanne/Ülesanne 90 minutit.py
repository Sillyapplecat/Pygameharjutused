import pygame
import random

pygame.init()


screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Ülesanne 4")

bg = pygame.image.load("white.jpg")
Ruut = pygame.image.load("Ruut.png")
PunaneRuut = pygame.image.load("punaneruut.png")
Barrier = pygame.image.load("block.png")


score = 0
font = pygame.font.Font(None, 36)
Barrier_width, Barrier_height = Barrier.get_size()
Area = [(0, 640)]
coords = [[random.randint(start, end - Barrier_width), random.randint(-screenY, 0), random.randint(2, 5)] for start, end in Area]
for i in range (10):
    posX = random.randint(1,screenX)
    posY = random.randint(1,screenY)
    speed = random.randint(1,5)
    coords.append([posX, posY, speed])



Ruut_x = (screenX - Ruut.get_width()) // 2
Ruut_y = screenY - Ruut.get_height() - 20
Ruut_speed = 5

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Ruut_x > 0:
        Ruut_x -= Ruut_speed
    if keys[pygame.K_d] and Ruut_x < 640 - Ruut.get_width():
        Ruut_x += Ruut_speed
    if keys[pygame.K_w] and Ruut_y > 0:
        Ruut_y -= Ruut_speed
    if keys[pygame.K_s] and Ruut_y < screenY - Ruut.get_height():
        Ruut_y += Ruut_speed


    screen.blit(bg, (0, 0))


    for Objekt in coords:
        Objekt[1] += Objekt[2]
        if Objekt[1] > screenY:
            Objekt[1] = random.randint(-100, -40)
            Objekt[0] = random.randint(0, 640 - Barrier_width)
            score += 1

        if pygame.Rect(Ruut_x, Ruut_y, Ruut.get_width(), Ruut.get_height()).colliderect(
                pygame.Rect(Objekt[0], Objekt[1], Barrier_width, Barrier_height)):
            Ruut = pygame.image.load("punaneruut.png")
            print("Mäng läbi!")
            print("Sinu mängu lõplik skoor on:", score)
            running = False
        screen.blit(Barrier, (Objekt[0], Objekt[1]))


    screen.blit(Ruut, (Ruut_x, Ruut_y))


    screen.blit(font.render(f"Skoor: {score}", True, (0, 0, 0)), (10, 10))

    pygame.display.flip()

pygame.quit()