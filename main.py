import math
import random
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import utility
from colors import LIGHT_RED, DARK_GRAY, LIGHT_GRAY, GRAY, LIGHT_BLUE, WHITE
from fruit import Fruit, draw_fruits
from function import Function
from graph import Graph
from settings import FPS, SCREEN, BORDER, FONT, WIDTH, HEIGHT

LIN_FUNC = (-1 / 2, 500)

#                x start, y start, length, height ...

slider1 = Slider(SCREEN, 10, 10, 80, 10, min=-1, max=1, step=0.1)
slider2 = Slider(SCREEN, 10, 30, 80, 10, min=-1, max=1, step=0.1)
slider3 = Slider(SCREEN, 10, 50, 80, 10, min=-1, max=1, step=0.1)
slider4 = Slider(SCREEN, 10, 70, 80, 10, min=-1, max=1, step=0.1)

if __name__ == '__main__':
    clock = pygame.time.Clock()

    graph = Graph(9)
    function = Function(graph.XY_offsets)
    function.points = function.linear_func_points(LIN_FUNC[0], LIN_FUNC[1])

    num_fruits = 150
    all_fruits = []
    for _ in range(num_fruits):
        all_fruits.append(Fruit(function.points_dict))

    # Screen window loop
    running = True
    while running:
        # Set the frame rates
        clock.tick(FPS)

        # Check for closure
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        # Fill background
        SCREEN.fill(DARK_GRAY)

        graph.draw_grid("Spot Size", "Spike Length")
        draw_fruits(all_fruits)
        function.graph_func()

        pygame_widgets.update(events)
        pygame.display.update()

pygame.quit()
