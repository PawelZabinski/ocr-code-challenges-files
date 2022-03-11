import pygame
import random
import math

FPS = 120
MODE = (600, 600)

BACKGROUND_COLOR = (20, 20, 30)
STREAK_COUNT = 100


def randomColour():
    return tuple(random.randint(30, 255) for _ in range(3))

class Streak:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        angle = random.uniform(0, 360)
        displacement = random.uniform(.5, 1.5)

        # Using the randomised angle and displacement, we can calculate the x and y axis in which the streak will be moved at each frame
        # SOH CAH TOA means that using an angle and the hypotenuse we can calculate x and y values.
        
        # cos(angle) ⋅ displacement [ hypotenuse ] = y value [ opposite ] 
        # sin(angle) ⋅ displacement [ hypotenuse ] = x value [ adjacent ]

        # Velocity of x
        self.vx = displacement * math.cos(math.radians(angle))

        # Velocity of y
        self.vy = displacement * math.sin(math.radians(angle))

        self.colour = randomColour()

        self.timer = 0
        self.timerMultiplier = random.uniform(1, 2)
        self.isEnded = False

    def getAngle(self):
        return math.atan2(self.vy, self.vx)

    def move(self):
        self.x += self.vx
        self.y -= self.vy

        self.timer += 1
        self.isEnded = self.timer >= FPS * self.timerMultiplier

    def draw(self, display):
        dx = 2 * math.cos(self.getAngle())
        dy = 2 * math.sin(self.getAngle())

        a = [int(self.x + dx), int(self.y - dy)]
        b = [int(self.x - dx), int(self.y + dy)]

        pygame.draw.line(display, self.colour, a, b, 1)


class Firework:
    def __init__(self, x, endY):
        self.x = x
        self.y = MODE[1]

        self.endY = endY
        self.isEnded = False

        self.velocity = random.uniform(3.5, 7)

        self.colour = randomColour()

    def move(self):
        self.y -= self.velocity
        self.isEnded = self.y <= self.endY

    def draw(self, display):
        a = [self.x, int(self.y + 20)]
        b = [self.x, int(self.y - 20)]

        pygame.draw.line(display, self.colour, a, b, 8)


def main():
    pygame.init()
    pygame.display.set_caption('Fireworks Festival')

    win = pygame.display.set_mode(MODE)
    clock = pygame.time.Clock()

    fireworks = [Firework(x=random.randint(0, MODE[0]), endY=random.uniform(
        10, MODE[1] / 2)) for _ in range(1)]

    streaks = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                fireworks.append(Firework(x=pos[0], endY=pos[1]))

        win.fill(BACKGROUND_COLOR)

        for firework in fireworks:
            firework.move()
            firework.draw(win)

            if firework.isEnded:
                streaks += [Streak(firework.x, firework.y)
                            for _ in range(random.randint(STREAK_COUNT - 20, STREAK_COUNT + 20))]
                fireworks.remove(firework)

        for streak in streaks:
            streak.move()
            streak.draw(win)

            if streak.isEnded:
                streaks.remove(streak)

        pygame.display.update()
        clock.tick(FPS)

        # Stats for performance and memory leaks
        print('Streaks:', len(streaks))
        print('Fireworks:', len(fireworks), end='\n'*3)


if __name__ == '__main__':
    main()
    pygame.quit()
