'''
Created on Oct 30, 2011

@author: Carke
'''
import pygame, Buttons
from pygame.locals import *
from Buttons import *
from SettingsWindow import SettingsWindow
from AboutWindow import AboutWindow
from InstructionsWindow import InstructionsWindow
MainMenu = pygame.display.set_mode([700,700])
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("01 - Challenge.ogg")
pygame.display.set_caption("Main Menu")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)
state = 0
x1=0
y1=0
MusicVolume = 1
BackButtonText = pygame.font.Font(None,44).render("Press Escape at any time to exit the game", 1, (0,0,0))

while state == 0:
    MainMenu = pygame.display.set_mode([700,700])
    pygame.display.set_caption("Main Menu")
    event = pygame.event.poll()
    MainMenu.fill([111,159,225])
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x1=event.pos[0] 
            y1=event.pos[1]
    SettingsButton = pygame.Rect(55,430, 280,70)
    PlayButton = pygame.Rect(100,225,260,140)
    InstructionsButton = pygame.Rect(375,225,260,140)
    AboutButton = pygame.Rect(350,430,280,70)
    MainMenu.blit(Logo.image, Logo)
    MainMenu.blit(InstructionsButtoninitial.image, InstructionsButtoninitial)
    MainMenu.blit(PlayButtoninitial.image, PlayButtoninitial)
    MainMenu.blit(SettingButtoninitial.image,SettingButtoninitial) 
    MainMenu.blit(AboutButtoninitial.image, AboutButtoninitial)
    MainMenu.blit(BackButtonText,(50,520))
    
    #Code for Settings Button Mouseover
    if SettingsButton.collidepoint((x1,y1)):
        MainMenu.blit(SettingButtonHover.image,SettingButtonHover)  
        if event.type == MOUSEBUTTONDOWN :
            SettingsWindow()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1

#code for controlling About Button Mouseover
    elif AboutButton.collidepoint((x1,y1)):
        MainMenu.blit(AboutButtonHover.image,AboutButtonHover)
        if event.type == MOUSEBUTTONUP: #code for About Menu
            AboutWindow()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
            
# Code for Play Button Mouseover
    elif PlayButton.collidepoint((x1,y1)):
            MainMenu.blit(PlayButtonHover.image,PlayButtonHover)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 1
#Code for Instruction Button Mouseover
    elif InstructionsButton.collidepoint((x1,y1)):
            MainMenu.blit(InstructionsButtonHover.image, InstructionsButtonHover)
            if event.type == MOUSEBUTTONUP:
                InstructionsWindow() 
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 1           

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
        
    
    