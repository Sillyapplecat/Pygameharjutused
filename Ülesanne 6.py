import pygame
pygame.init()


pygame.mixer.music.load("Crazyfrog.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


lBlue = [153, 204, 255]
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("PingPongPing")
clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 36)
score = 0
nextBallScore = 10


ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [20, 20])

balls = [{
    "rect": pygame.Rect(320, 240, 20, 20),
    "speedX": 4,
    "speedY": 4
}]


padWidth = 120
padHeight = 20
pad = pygame.image.load("pad.png")
pad = pygame.transform.scale(pad, [padWidth, padHeight])
padRect = pad.get_rect()
padRect.x = screenX // 2 - padWidth // 2
padRect.y = int(screenY / 1.5)
padSpeed = 5

running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if keys[pygame.K_LEFT]:
        padRect.x -= padSpeed
    if keys[pygame.K_RIGHT]:
        padRect.x += padSpeed


    padRect.x = max(0, min(padRect.x, screenX - padWidth))


    for ball in balls:
        ball["rect"].x += ball["speedX"]
        ball["rect"].y += ball["speedY"]

        # Seinad
        if ball["rect"].left <= 0 or ball["rect"].right >= screenX:
            ball["speedX"] = -ball["speedX"]
        if ball["rect"].top <= 0:
            ball["speedY"] = -ball["speedY"]
        if ball["rect"].bottom >= screenY:
            running = False  # mäng läbi


        if ball["rect"].colliderect(padRect) and ball["speedY"] > 0:
            ball["speedY"] = -ball["speedY"]
            score += 1


            if score >= nextBallScore:
                nextBallScore += 10
                newBall = {
                    "rect": pygame.Rect(padRect.centerx, padRect.y - 20, 20, 20),
                    "speedX": 4,
                    "speedY": -4
                }
                balls.append(newBall)


    screen.fill(lBlue)
    for ball in balls:
        screen.blit(ballImage, ball["rect"])
    screen.blit(pad, padRect)

    text = font.render("Skoor: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
