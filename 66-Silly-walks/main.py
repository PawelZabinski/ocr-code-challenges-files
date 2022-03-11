import pygame
import random
from datetime import datetime

WIDTH = HEIGHT = 500
BACKGROUND = (31, 30, 30)
FPS = 15

LINE_LENGTH = 25

TIME = 0.25

PATH_COUNT = 4
PATH_COLOURS = [
    (235, 45, 127),
    (66, 135, 245),
    (245, 78, 66),
    (66, 245, 99)
]

PARTICLE_COUNT = 100
PARTICLE_COLOUR = (50, 50, 50)
PARTICLE_RADIUS = 2


class Path:
    def __init__(self, colour):
        self.colour = colour
        self.points = [(WIDTH / 2, HEIGHT / 2)]

        self.time = datetime.now()

    def move(self):
        # Check if it has been 0.5 seconds since last move
        currentTime = datetime.now()
        timeDelta = currentTime - self.time
        if not timeDelta.total_seconds() >= TIME:
            return

        # Change self.time, because new move is being calculated
        self.time = currentTime

        moves = [(0, LINE_LENGTH), (LINE_LENGTH, 0),
                 (0, -LINE_LENGTH), (-LINE_LENGTH, 0)]

        move = moves[random.randrange(0, 4)]

        newPoint = tuple(map(sum, zip(self.points[-1], move)))
        self.points.append(newPoint)

    def draw(self, screen):
        if len(self.points) < 2:
            return
        pygame.draw.lines(screen, self.colour, False, self.points)


class Particle:
    def __init__(self, colour=PARTICLE_COLOUR):
        self.colour = colour

        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

    def move(self):
        # Change x axis
        if self.x < WIDTH - 50 and (self.x < 50 or random.getrandbits(1)):
            self.x += random.randint(0, WIDTH / 2)
        else:
            self.x -= random.randint(0, WIDTH / 2)

        # Change y axis
        if self.y < HEIGHT - 50 and (self.y < 50 or random.getrandbits(1)):
            self.y += random.randint(0, HEIGHT / 2)
        else:
            self.y -= random.randint(0, HEIGHT / 2)

        # Set boundaries
        self.x = min(WIDTH, max(0, self.x))
        self.y = min(HEIGHT, max(0, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour,
                           (self.x, self.y), PARTICLE_RADIUS)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Silly walks')

    clock = pygame.time.Clock()

    paths = [Path(PATH_COLOURS[i]) for i in range(PATH_COUNT)]
    particles = [Particle() for _ in range(PARTICLE_COUNT)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(BACKGROUND)

        for particle in particles:
            particle.move()
            particle.draw(screen)

        for path in paths:
            path.move()
            path.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
