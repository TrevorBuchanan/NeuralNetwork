# By Trevor Buchanan
# Visualization inspired by Sebastian Lague (https://www.youtube.com/watch?v=hfMk-kjRv4c&t=2378s)

import pygame
import pygame_widgets

from Visualization.settings import FPS
from Visualization.manual_visualization import ManualVisualization


if __name__ == '__main__':
    clock = pygame.time.Clock()

    manual_visualization = ManualVisualization(200)
    # auto_visualization = AutoVisualization(200, [2, 5, 5, 5, 2])

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

        manual_visualization.draw_visualization()
        # auto_visualization.draw_visualization()

        pygame_widgets.update(events)
        pygame.display.update()

pygame.quit()
