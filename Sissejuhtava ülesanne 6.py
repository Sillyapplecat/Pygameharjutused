import pygame, random

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("Muusika")

sounds = ['Crazyfrog.mp3']
pygame.mixer.music.load(random.choice(sounds))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

import pygame, random

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("Muusika")

hit_sound = pygame.mixer.Sound('Crazyfrog.mp3')
pygame.mixer.Sound.play(hit_sound)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()