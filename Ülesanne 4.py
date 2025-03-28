import pygame
import random

pygame.init()


screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Ülesanne 4")


bg = pygame.image.load("bg_rally.jpg")
red_car = pygame.image.load("f1_red.png")
blue_car = pygame.image.load("f1_blue.png")


font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 60)

car_width, car_height = blue_car.get_size()
road_sections = [(150, 230), (250, 330), (400, 490)]

clock = pygame.time.Clock()


def reset_game():
    """Funktsioon mängu uuesti alustamiseks."""
    global score, red_car_x, red_car_y, game_over, coords

    score = 0
    red_car_x = (screenX - red_car.get_width()) // 2
    red_car_y = screenY - red_car.get_height() - 20
    game_over = False
    coords = [[random.randint(start, end - car_width), random.randint(-screenY, 0), random.randint(2, 5)] for start, end
              in road_sections]



reset_game()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset_game()
            if event.key == pygame.K_q:
                running = False


    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_a] and red_car_x > 150:
            red_car_x -= 5
        if keys[pygame.K_d] and red_car_x < 490 - red_car.get_width():
            red_car_x += 5
        if keys[pygame.K_w] and red_car_y > 0:
            red_car_y -= 5
        if keys[pygame.K_s] and red_car_y < screenY - red_car.get_height():
            red_car_y += 5

    screen.blit(bg, (0, 0))

    if not game_over:
        for car in coords:
            car[1] += car[2]
            if car[1] > screenY:
                car[1] = random.randint(-100, -40)
                car[0] = random.randint(150, 490 - car_width)
                score += 1

            if pygame.Rect(red_car_x, red_car_y, red_car.get_width(), red_car.get_height()).colliderect(
                    pygame.Rect(car[0], car[1], car_width, car_height)):
                game_over = True

            screen.blit(blue_car, (car[0], car[1]))

    screen.blit(red_car, (red_car_x, red_car_y))
    screen.blit(font.render(f"Skoor: {score}", True, (255, 255, 255)), (10, 10))

    if game_over:
        text1 = game_over_font.render("Game Over", True, (255, 0, 0))
        text2 = game_over_font.render(f"Final Score: {score}", True, (255, 255, 255))
        text3 = font.render("Vajuta ENTER, et uuesti alustada", True, (0, 0, 0))
        text4 = font.render("Vajuta Q, et mäng kinni panna", True, (0, 0, 0))
        screen.blit(text1, (screenX // 2 - text1.get_width() // 2, 180))
        screen.blit(text2, (screenX // 2 - text2.get_width() // 2, 240))
        screen.blit(text3, (screenX // 2 - text3.get_width() // 2, 300))
        screen.blit(text4, (screenX // 2 - text4.get_width() // 2, 340))

    pygame.display.flip()

pygame.quit()
