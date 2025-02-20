import pygame
pygame.init()

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("Ülesanne 2")

bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])

sel = pygame.image.load("seller.png")
sel = pygame.transform.scale(sel, [200, 250])
screen.blit(sel,[100,180])

chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [200, 200])
screen.blit(chat,[230,70])

vikk = pygame.image.load("VikkTulevik.png")
vikk = pygame.transform.scale(vikk, [300, 75])
screen.blit(vikk,[5,5])

mook = pygame.image.load("Mõõk.png")
mook = pygame.transform.scale(mook, [110, 70])
screen.blit(mook,[530,150])

kook = pygame.image.load("kook.png")
kook = pygame.transform.scale(kook, [110, 90])
screen.blit(kook,[430,210])

font = pygame.font.Font(pygame.font.match_font('arial'), 25)
font.set_underline(False)
text = font.render("Tere, olen Kairiin", True, [255,255,255])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [330-text_width/2,160-text_height/2])
pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()