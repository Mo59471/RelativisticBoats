import pygame
from Boat import Boat
from Button import Button
from Checkbox import Checkbox
from Clock import Clock
from Slider import Slider

def display(screen):

    # Draw background
    backImg = pygame.image.load("Background.png")
    screen.blit(backImg, (0,0))

    # Draw sidebar
    sideBarImg = pygame.image.load("Sidebar.png")
    screen.blit(sideBarImg, (0,0))

    # Update screen
    pygame.display.flip()


def getdt():
    pass

# Initialize data
screen = pygame.display.set_mode((1150,850))
clicked = False

#Initialize classes
buttonData = [
    {"label" : "p l a y", "x": 50, "y": 50, "w": 200, "h": 50, "shadowC": (0,0,0), 
    "img": pygame.image.load("StartButtonNorm.png"), "hovImg": pygame.image.load("StartButtonHov.png")}
            ]
button = []

# Appliction loop
running = True
while running:

    # Event Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    # Method calls
    display(screen)
