import pygame
pygame.init()

#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("My Screen")

#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Harjutamine")
#screen.fill([204, 255, 204])

#lisame teksti
#font = pygame.font.Font(None, 30)
#font = pygame.font.Font(pygame.font.match_font('arial'), 50)
#font = pygame.font.SysFont("Tahoma", 50)

# = font.render("Hello PyGame", True, [0,0,0])
#screen.blit(text, [200,200])


#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Harjutamine")
#screen.fill([204, 255, 204])


#font = pygame.font.Font(pygame.font.match_font('arial'), 50)
#text = font.render("Hello PyGame", True, [0,0,0])


#text_width = text.get_rect().width
#text_height = text.get_rect().height

#screen.blit(text, [320,240])

#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Harjutamine")
#screen.fill([204, 255, 204])


#font = pygame.font.Font(pygame.font.match_font('arial'), 50)
#font.set_underline(True)
#text = font.render("Hello PyGame", True, [0,0,0])


#text_width = text.get_rect().width
#text_height = text.get_rect().height

#screen.blit(text, [320-text_width/2,240-text_height/2])

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])


bg = pygame.image.load("img/bg.jpg")
screen.blit(bg,[0,0])

youWin = pygame.image.load("img/youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])

pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()