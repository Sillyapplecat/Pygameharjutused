import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)

# graafika laadimine
#ball = pygame.image.load("ball.png")

# kiirus ja asukoht
#posX, posY = 0, 0

gameover = False
#while not gameover:
    # mängu sulgemine ristist
    #events = pygame.event.get()
    #for i in pygame.event.get():
        #if i.type == pygame.QUIT:
            #sys.exit()

    # pildi lisamine ekraanile
    #screen.blit(ball, (posX, posY))

    # graafika kuvamine ekraanil
    #pygame.display.flip()
    #running = True
    #while running:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #running = False


    #pygame.quit()

#import pygame, sys

#pygame.init()

# värvid
#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

# ekraani seaded
#screenX = 640
#screenY = 480
#screen = pygame.display.set_mode([screenX, screenY])
#pygame.display.set_caption("Animeerimine")
#screen.fill(lBlue)

# graafika laadimine
#ball = pygame.image.load("ball.png")

# kiirus ja asukoht
#posX, posY = 0, 0
#speedX = 1

#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False

    # pildi lisamine ekraanile
    #screen.blit(ball, (posX, posY))

    #posX += speedX

    # graafika kuvamine ekraanil
    #pygame.display.flip()

#pygame.quit()

#import pygame, sys

#pygame.init()

# värvid
#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

# ekraani seaded
#screenX = 640
#screenY = 480
#screen = pygame.display.set_mode([screenX, screenY])
#pygame.display.set_caption("Animeerimine")
#screen.fill(lBlue)
#clock = pygame.time.Clock()

# graafika laadimine
#ball = pygame.image.load("ball.png")

# kiirus ja asukoht
#posX, posY = 0, 0
#speedX = 3

#running = True
#while running:
    #clock.tick(60)
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False

    # pildi lisamine ekraanile
    #screen.blit(ball, (posX, posY))

    #posX += speedX

    # graafika kuvamine ekraanil
    #pygame.display.flip()
    #screen.fill(lBlue)

#pygame.quit()

# import pygame, sys
#
# pygame.init()
#
# # värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# lBlue = [153, 204, 255]
#
# # ekraani seaded
# screenX = 640
# screenY = 480
# screen = pygame.display.set_mode([screenX, screenY])
# pygame.display.set_caption("Animeerimine")
# screen.fill(lBlue)
# clock = pygame.time.Clock()
#
# # graafika laadimine
# ball = pygame.image.load("ball.png")
#
# # kiirus ja asukoht
# posX, posY = 0, 0
# speedX, speedY = 3, 4
#
# running = True
# while running:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # pildi lisamine ekraanile
#     screen.blit(ball, (posX, posY))
#
#     posX += speedX
#     posY += speedY
#
#     # kui puudub ääri, siis muudab suunda
#     if posX > screenX - ball.get_rect().width or posX < 0:
#         speedX = -speedX

    #if posY > screenY - ball.get_rect().height or posY < 0:
        #speedY = -speedY

    # graafika kuvamine ekraanil
    #pygame.display.flip()
    #screen.fill(lBlue)

#pygame.quit()

# import pygame, sys, random
#
# pygame.init()
#
# # värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# lBlue = [153, 204, 255]
#
# # ekraani seaded
# screenX = 640
# screenY = 480
# screen = pygame.display.set_mode([screenX, screenY])
# pygame.display.set_caption("Animeerimine")
# screen.fill(lBlue)
# clock = pygame.time.Clock()
#
# # kiirus ja asukoht
# posX, posY = 0, 0
# speedX, speedY = 3, 3
#
# # koordinaatide loomine ja lisamine massiivi
# coords = []
# for i in range(10):
#     posX = random.randint(1, screenX)
#     posY = random.randint(1, screenY)
#     coords.append([posX, posY])
#
# running = True
# while running:
#     clock.tick(120)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # loendist koordinaadid
#     for i in range(len(coords)):
#         pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
#
#     pygame.display.flip()
#     screen.fill(lBlue)
# pygame.quit()

# import pygame, sys, random
#
# pygame.init()
#
# # värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# lBlue = [153, 204, 255]
#
# # ekraani seaded
# screenX = 640
# screenY = 480
# screen = pygame.display.set_mode([screenX, screenY])
# pygame.display.set_caption("Animeerimine")
# screen.fill(lBlue)
# clock = pygame.time.Clock()
#
# # kiirus ja asukoht
# posX, posY = 0, 0
# speedX, speedY = 3, 3
#
# # koordinaatide loomine ja lisamine massiivi
# coords = []
# for i in range(10):
#     posX = random.randint(1, screenX)
#     posY = random.randint(1, screenY)
#     coords.append([posX, posY])
#
# running = True
# while running:
#     clock.tick(120)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # loendist koordinaadid
#     for i in range(len(coords)):
#         pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
#         coords[i][1] += 1
#         # kui jõuab alla, siis muudame ruduu alguspunkti
#         if coords[i][1] > screenY:
#             coords[i][1] = random.randint(-40, -10)
#             coords[i][0] = random.randint(0, screenX)
#
#     pygame.display.flip()
#     screen.fill(lBlue)
# pygame.quit()

import pygame, sys, random

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

#koordinaatide loomine ja lisamine massiivi
coords = []
for i in range (10):
    posX = random.randint(1,screenX)
    posY = random.randint(1,screenY)
    speed = random.randint(1,5)
    coords.append([posX, posY, speed])

running = True
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += coords[i][2]
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)

    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()
