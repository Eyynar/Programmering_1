import pygame
import sys
from avatar import Avatar


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("GAMER!")

        self.bg_color = (230, 230, 230)

        self.avatar = Avatar(self)

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

            pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.avatar.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.avatar.moving_left = True
                if event.key == pygame.K_UP:
                    self.avatar.jumping_up = True
                if event.key == pygame.K_DOWN:
                    self.avatar.jumping_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.avatar.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.avatar.moving_left = False

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.avatar.update()
        self.avatar.draw()


game = Game()
game.run_game()

