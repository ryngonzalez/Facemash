'''
Created on Nov 2, 2011

@author: Carke
'''
import pygame
from pygame.locals import *
from Buttons import *
        
def InstructionsWindow():
    global InstructionsTitleText
    pygame.display.quit()
    setting = 0
    while setting == 0:
        InstructionsMenu = pygame.display.set_mode([500,500])
        pygame.display.set_caption("Instructions")
        InstructionsMenu.fill([111,159,225])
        InstructionsMenu.blit(InstructionsTitleText.image,InstructionsTitleText)
        BackButtonText = pygame.font.Font(None,32).render("Press Escape to go back.", 1, (0,0,0))
        InstructionsMenu.blit(BackButtonText,(100,450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                setting = 1