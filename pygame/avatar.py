import pygame


class Avatar:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/mario.png")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        self.jumping_up = False
        self.jumping_down = False
        self.jump_height = 200
        self.jump_duration = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 2
        if self.moving_left:
            self.rect.x -= 2

        if self.jumping_up:
            self.rect.y -= 2
            self.jump_duration += 2
            if self.jump_duration >= self.jump_height:
                self.jumping_up = False
                self.jumping_down = True
        if self.jumping_down:
            self.rect.y += 2
            self.jump_duration += 2
            if self.jump_duration >= self.jump_height*2:
                self.jumping_down = False
                self.jump_duration = 0
