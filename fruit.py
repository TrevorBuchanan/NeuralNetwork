import random

import pygame

from colors import LIGHT_RED, LIGHT_BLUE
from settings import WIDTH, HEIGHT, SCREEN
from utility import is_under_func


# Generate random positions (in graph with 9 line scale)
def generate_random_pos():
    x = random.randint(100, WIDTH - 10)
    y = random.randint(10, HEIGHT - 100)
    pos = [x, y]

    return pos


def draw_fruits(fruits):
    for fruit in fruits:
        if fruit.poisonous:
            pygame.draw.circle(SCREEN, LIGHT_RED, fruit.position, 8)
        else:
            pygame.draw.circle(SCREEN, LIGHT_BLUE, fruit.position, 8)


class Fruit:
    def __init__(self, points):
        self.poisonous = bool(random.getrandbits(1))
        self.position = generate_random_pos()
        while self.poisonous and is_under_func(self.position, points):
            self.position = generate_random_pos()
        while not self.poisonous and not is_under_func(self.position, points):
            self.position = generate_random_pos()
