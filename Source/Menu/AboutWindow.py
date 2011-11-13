'''
Created on Nov 1, 2011

@author: Carke
'''
import pygame
from pygame.locals import *
from Buttons import *

def AboutWindow():
    pygame.display.quit()
    setting = 0
    while setting == 0:
        AboutMenu = pygame.display.set_mode([500,500])
        pygame.display.set_caption("About")
        AboutMenu.fill([111,159,225])
        AboutMenu.blit(AboutTitleText.image, AboutTitleText)
        BackButtonText = pygame.font.Font(None,32).render("Press Escape to go back.", 1, (0,0,0))
        AboutMenu.blit(BackButtonText,(100,450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                setting = 1