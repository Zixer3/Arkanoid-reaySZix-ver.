import pygame
from main import Palka
from main import Kirpich

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOWS_WIDHT = 1000
        self.WINDOWS_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOWS_WIDHT, self.WINDOWS_HEIGHT))
        self.palka = Palka(self.WINDOWS_WIDHT // 2, self.WINDOWS_HEIGHT - 15)
        self.Kirpich = Kirpich(10, 10)

    def get_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def start(self):
        while True:
            self.draw()
            self.get_keys()
    def draw(self):
        self.palka.draw(self.screen)
        pygame.display.flip()
game = Game()
game.start()