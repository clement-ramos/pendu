import pygame
from button import *
from pygame.locals import *

pygame.init()

def test():
    return 'Bruhhhhhh'


def ESC_now(running,event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running=False
    return running

def main_menu():
    running=True
    while running:
        events=pygame.event.get()
        for event in events:
            running=ESC_now(running,event)
   
        screen.blit(BG_MENU, (0, 0))

        MENU_TEXT = get_font(100).render("HangMan", True, font_color)
        MENU_RECT = MENU_TEXT.get_rect(center=(430, 100))

        screen.blit(MENU_TEXT, MENU_RECT)
        
        button1.draw()
        # button2.draw()
        # button3.draw()

        pygame.display.update()
        clock.tick(60)



#Classic setup for pygame
# pygame.init()

screen = pygame.display.set_mode((880,500))
pygame.display.set_caption("GUI Menu")

clock = pygame.time.Clock()

BG_MENU = pygame.image.load("assets\BG-menu.png")

button1 = Button("Play",screen,200,40,(50,450),6,test())
# button2 = Button("Options",screen,200,40,(340,450),6)
# button3 = Button("Scoreboard",screen,200,40,(630,450),6)

main_menu()
