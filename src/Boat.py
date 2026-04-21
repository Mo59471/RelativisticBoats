import pygame

class Boat:
    def __init__(self, x, img):
        self.x = x
        self.img = img
        self.speed = 0
        
    def display(self, screen, v):
        screen.blit(self.img, (self.x,0))
        self.x == self.x + v

    def move(self, v):
        pass
    
    def update(self):
        pass
    
    def lorentzContraction(self, lorentzC):
        pass
        