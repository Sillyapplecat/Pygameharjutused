import pygame
pygame.init()


lBlue = [153, 204, 255]
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("PingPongPing")
clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 36)
score = 0


ball = pygame.Rect(320, 240, 20, 20)
ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [ball.width, ball.height])
ballSpeedX = 4
ballSpeedY = 4


padWidth = 120
padHeight = 20
pad = pygame.image.load("pad.png")
pad = pygame.transform.scale(pad, [padWidth, padHeight])
padRect = pad.get_rect()
padRect.x = 0
padRect.y = int(screenY / 1.5)
padSpeed = 5
padDirection = 1

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ball.x += ballSpeedX
    ball.y += ballSpeedY


    if ball.left <= 0 or ball.right >= screenX:
        ballSpeedX = -ballSpeedX
    if ball.top <= 0:
        ballSpeedY = -ballSpeedY
    if ball.bottom >= screenY:
        score -= 1
        ball.x, ball.y = 320, 240
        ballSpeedY = 4


    padRect.x += padSpeed * padDirection
    if padRect.left <= 0 or padRect.right >= screenX:
        padDirection *= -1

    if ball.colliderect(padRect) and ballSpeedY > 0:
        ballSpeedY = -ballSpeedY
        score += 1


    screen.fill(lBlue)
    screen.blit(ballImage, ball)
    screen.blit(pad, padRect)


    text = font.render("Skoor: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()