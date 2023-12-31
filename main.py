import random

import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from colors import LIGHT_RED, DARK_GRAY, LIGHT_GRAY, GRAY, LIGHT_BLUE, WHITE, BLUE, RED
from fruit import Fruit, draw_fruits
from function import Function
from graph import Graph
from neuralnetwork import NeuralNet
from settings import FPS, SCREEN, BORDER, FONT, WIDTH, HEIGHT


#                x start, y start, length, height ...
slider1 = Slider(SCREEN, 10, 40, 80, 10, min=-1, max=1, step=0.05, initial=random.uniform(-1, 1))
slider2 = Slider(SCREEN, 10, 60, 80, 10, min=-1, max=1, step=0.05, initial=random.uniform(-1, 1))
slider3 = Slider(SCREEN, 10, 80, 80, 10, min=-1, max=1, step=0.05, initial=random.uniform(-1, 1))
slider4 = Slider(SCREEN, 10, 100, 80, 10, min=-1, max=1, step=0.05, initial=random.uniform(-1, 1))

slider5 = Slider(SCREEN, 10, 180, 80, 10, min=-100, max=100, step=0.1, initial=random.uniform(-100, 100))
slider6 = Slider(SCREEN, 10, 200, 80, 10, min=-100, max=100, step=0.1, initial=random.uniform(-100, 100))
# slider7 = Slider(SCREEN, 10, 220, 80, 10, min=-1, max=1, step=0.05)
# slider8 = Slider(SCREEN, 10, 240, 80, 10, min=-1, max=1, step=0.05)

if __name__ == '__main__':
    clock = pygame.time.Clock()

    NN = NeuralNet([2, 2])
    graph = Graph(9)
    fruit_function = Function(graph.XY_offsets)
    decision_function = Function(graph.XY_offsets)
    fruit_function.points = fruit_function.linear_func_points(-1 / 2, 500)

    num_fruits = 150
    all_fruits = []
    for _ in range(num_fruits):
        all_fruits.append(Fruit(fruit_function.points_dict))

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

        for fruit in all_fruits:
            if NN.classify(fruit.position):
                pygame.draw.circle(SCREEN, BLUE, fruit.position, 5)
            else:
                pygame.draw.circle(SCREEN, RED, fruit.position, 5)

        NN.manual_set_weights([slider1.value, slider2.value, slider3.value, slider4.value])
        NN.manual_set_biases([slider5.value, slider6.value])
        decision_function.points = NN.get_decision_boundary()
        decision_function.graph_func()

        text = FONT.render("Weights", True, WHITE)
        SCREEN.blit(text, [10, 10])
        text = FONT.render("Biases", True, WHITE)
        SCREEN.blit(text, [10, 150])
        pygame_widgets.update(events)
        pygame.display.update()

pygame.quit()
