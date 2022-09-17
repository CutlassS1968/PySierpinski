from random import Random

import pygame
import math

WIDTH = 800
HEIGHT = 800

# Field of the camera's view
FOV = 100 * (math.pi / 180)

# Width of each line drawn to the screen
RES_SCALE = 6

# Number of rays in fov_cone scale based on size of window
RAY_COUNT = 3

# int((WIDTH / (FOV / (360 * (math.pi/180)))) / RES_SCALE)

# Amount the user rotates their fov
ROTATION_UNITS = 2 * (math.pi / 180)

# Amount the user moves in the world
MOVE_UNITS = .666

# Default of each ray (View Distance) = math.sqrt(math.pow(HEIGHT, 2) + math.pow(WIDTH, 2))
GR = 300
# math.sqrt(math.pow(HEIGHT, 2) + math.pow(WIDTH, 2))

# Distance till light = 0; = GR
LIGHT_DIST = 5000

# CAMERA_PLANE_DIST = math.fabs((WIDTH / 2) / math.tan((FOV * 180/math.pi) / 2))
CAMERA_PLANE_DIST = (WIDTH/2) / (math.tan(FOV/2))

# Height of walls
WALL_HEIGHT = 40


class Hexagon:
    def __init__(self):
        self.center = (WIDTH / 2, HEIGHT / 2)
        self.random = Random()
        self.random.seed()
        self.points = []
        # self.new_points = []
        self.gen_points()
        self.cur_point = (0, 0)


    def gen_points(self):
        rad_slice = (360.0 / RAY_COUNT) * (math.pi / 180)
        random_point = self.random.randint(0,5)
        p1 = self.center
        for i in range(RAY_COUNT):
            x = (p1[0] + (GR * math.cos(rad_slice * i)))
            y = (p1[1] + (GR * math.sin(rad_slice * i)))
            p2 = x, y
            self.points.append(p2)
            if i == random_point:
                self.cur_point = p2

    def draw(self, screen):
        for p in self.points:
            pygame.draw.circle(screen, (255, 255, 255), p, 3)

        # for p in self.new_points:
        #     pygame.draw.circle(screen, (255, 0, 0), p, 3)

    def update(self):
        nex_point = self.random.randint(0, RAY_COUNT - 1)
        p1 = self.cur_point
        p2 = self.points[nex_point]
        p4 = ((2 * (p1[0] - p2[0]))/3, (2*(p1[1]-p2[1]))/3)
        p5 = (p1[0]-p4[0], p1[1]-p4[1])
        self.points.append(p5)
        self.cur_point = p5
        # p3 = ()
        # self.new_points.append(p4)
        # self.cur_point = nex_point
        # print(self.cur_point)


class Display:

    def __init__(self):
        pygame.init()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((0, 101, 103))
        self.react = self.image.get_rect()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def get_screen(self):
        return self.screen

    def update(self):
        pygame.display.flip()


class Main:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PySierpinski")
        self.display = Display()
        self.hexagon = Hexagon()
        self.running = True
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        lc, rc, mc = [], [], []
        while self.running:
            keys = pygame.key.get_pressed()
            # Look through all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.hexagon.update()
            self.hexagon.draw(self.display.get_screen())

            # Tick the clock
            # pygame.time.delay()
            self.clock.tick(60)
            self.display.update()

        pygame.quit()


main = Main()
