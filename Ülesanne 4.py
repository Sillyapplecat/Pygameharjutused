import pygame
import random

pygame.init()


screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Ülesanne 4")

bg = pygame.image.load("bg_rally.jpg")
red_car = pygame.image.load("f1_red.png")
blue_car = pygame.image.load("f1_blue.png")


score = 0
font = pygame.font.Font(None, 36)
car_width, car_height = blue_car.get_size()
road_sections = [(150, 230), (250, 330), (400, 490)]
coords = [[random.randint(start, end - car_width), random.randint(-screenY, 0), random.randint(2, 5)] for start, end in road_sections]


red_car_x = (screenX - red_car.get_width()) // 2
red_car_y = screenY - red_car.get_height() - 20
red_car_speed = 5

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and red_car_x > 150:
        red_car_x -= red_car_speed
    if keys[pygame.K_d] and red_car_x < 490 - red_car.get_width():
        red_car_x += red_car_speed
    if keys[pygame.K_w] and red_car_y > 0:
        red_car_y -= red_car_speed
    if keys[pygame.K_s] and red_car_y < screenY - red_car.get_height():
        red_car_y += red_car_speed


    screen.blit(bg, (0, 0))


    for car in coords:
        car[1] += car[2]
        if car[1] > screenY:
            car[1] = random.randint(-100, -40)
            car[0] = random.randint(150, 490 - car_width)
            score += 1

        if pygame.Rect(red_car_x, red_car_y, red_car.get_width(), red_car.get_height()).colliderect(
                pygame.Rect(car[0], car[1], car_width, car_height)):
            print("Mäng läbi!")
            print(score)
            running = False
        screen.blit(blue_car, (car[0], car[1]))


    screen.blit(red_car, (red_car_x, red_car_y))


    screen.blit(font.render(f"Skoor: {score}", True, (255, 255, 255)), (10, 10))

    pygame.display.flip()

pygame.quit()