import pygame
import random
import sys


pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ringid")


BACKGROUND_COLOR = (173, 216, 230)
font = pygame.font.SysFont(None, 36)


pygame.mixer.music.load("crazyfrog.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


INITIAL_RADIUS = 10
MAX_CIRCLES = 10

class Ring:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def grow(self):
        self.radius += 2

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, 2)

rings = []
score = 0


running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            rings.append(Ring(x, y, INITIAL_RADIUS, color))
            score += 1

            if len(rings) > MAX_CIRCLES:
                rings.pop(0)

            for ring in rings:
                ring.grow()


    for ring in rings:
        ring.draw(screen)


    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
