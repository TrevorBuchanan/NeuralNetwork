import random

import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from colors import LIGHT_RED, DARK_GRAY, LIGHT_GRAY, GRAY, LIGHT_BLUE, WHITE, BLUE, RED, BLACK
from fruit import Fruit, draw_fruits
from function import Function
from graph import Graph
from neuralnetwork import NeuralNet
from settings import FPS, SCREEN, BORDER, FONT, WIDTH, HEIGHT


#                x start, y start, length, height ...
# Weights 1 sliders
slider1 = Slider(SCREEN, 10, 40, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider2 = Slider(SCREEN, 10, 60, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider3 = Slider(SCREEN, 10, 80, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider4 = Slider(SCREEN, 10, 100, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider5 = Slider(SCREEN, 10, 120, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider6 = Slider(SCREEN, 10, 140, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))

# Biases 1 sliders
slider7 = Slider(SCREEN, 10, 200, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider8 = Slider(SCREEN, 10, 220, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))

slider9 = Slider(SCREEN, 10, 240, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))

# Weights 2 sliders
slider10 = Slider(SCREEN, 10, 300, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider11 = Slider(SCREEN, 10, 320, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider12 = Slider(SCREEN, 10, 340, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider13 = Slider(SCREEN, 10, 360, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider14 = Slider(SCREEN, 10, 380, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider15 = Slider(SCREEN, 10, 400, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))

# Biases 1 sliders
slider16 = Slider(SCREEN, 10, 460, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))
slider17 = Slider(SCREEN, 10, 480, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25))


if __name__ == '__main__':
    clock = pygame.time.Clock()

    NN = NeuralNet([2, 3, 2])
    # NN = NeuralNet([2, 2])
    graph = Graph(9)
    fruit_function = Function(graph.XY_offsets)
    fruit_function.points = fruit_function.linear_func_points(-1 / 2, 500)

    num_fruits = 1000
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
        x = 0
        while 0 <= x <= BORDER.width:
            y = 0
            while 0 <= y <= BORDER.height:
                if NN.classify((x, y)):
                    pygame.draw.circle(SCREEN, LIGHT_BLUE, (x, y), 5)
                else:
                    pygame.draw.circle(SCREEN, LIGHT_RED, (x, y), 5)
                y += 10
            x += 10

        # draw_fruits(all_fruits)
        # for fruit in all_fruits:
        #     if NN.classify(fruit.position):
        #         pygame.draw.circle(SCREEN, WHITE, fruit.position, 5)
        #     else:
        #         pygame.draw.circle(SCREEN, BLACK, fruit.position, 5)

        NN.manual_set_weights([slider1.value, slider2.value, slider3.value,
                               slider4.value, slider5.value, slider6.value,
                               slider10.value, slider11.value, slider12.value,
                               slider13.value, slider14.value, slider15.value])
        NN.manual_set_biases([slider7.value, slider8.value, slider9.value, slider16.value, slider17.value])

        text = FONT.render("Weights 1", True, WHITE)
        SCREEN.blit(text, [10, 10])
        text = FONT.render("Biases 1", True, WHITE)
        SCREEN.blit(text, [10, 170])
        text = FONT.render("Weights 2", True, WHITE)
        SCREEN.blit(text, [10, 270])
        text = FONT.render("Biases 2", True, WHITE)
        SCREEN.blit(text, [10, 430])
        pygame_widgets.update(events)

        pygame.display.update()

pygame.quit()
