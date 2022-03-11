import pygame
import random

FPS = 10
WIDTH = 300
HEIGHT = 225

BACKGROUND = pygame.image.load('milkyway.jpg')
STARS = 100

STAR_COLOURS = [
    (158, 174, 249),
    (204, 215, 252),
    (249, 247, 252),
    (253, 255, 216),
    (254, 243, 171),
    (248, 212, 169)
]

class Star:
    def __init__(self):
        self.x = random.randint(15, WIDTH - 15)
        self.y = random.randint(15, HEIGHT - 15)

        self.standardColour = random.choice(STAR_COLOURS)

        self.brightness = 0.5

    def colour(self):
        return tuple(i * self.brightness for i in self.standardColour)

    def changeBrightness(self):
        if self.brightness >= 1:
            self.brightness -= random.uniform(0, 0.5)
        else:
            self.brightness += random.uniform(0, 0.5)

        self.brightness = max(0.4, min(1, self.brightness))

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour(),
                         pygame.Rect(self.x, self.y, 1, 1), 1)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Galaxy song')

    stars = [Star() for _ in range(STARS)]

    while True:
        screen.blit(BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        for star in stars:
            star.changeBrightness()
            star.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
