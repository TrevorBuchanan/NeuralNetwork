# By Trevor Buchanan
# Visualization inspired by Sebastian Lague (https://www.youtube.com/watch?v=hfMk-kjRv4c&t=2378s)

import pygame
import pygame_widgets

from Visualization.colors import WHITE
from Visualization.manual_visualization import ManualVisualization
from Visualization.auto_visualization import AutoVisualization
from Visualization.settings import FPS, SCREEN, FONT, BORDER

if __name__ == '__main__':
    clock = pygame.time.Clock()

    manual_visualization = ManualVisualization(100)
    # auto_visualization = AutoVisualization(100, [2, 3, 3, 2])

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

        fps = str(int(clock.get_fps()))
        text = FONT.render(f"FPS: {fps}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 100, 10])

        pygame_widgets.update(events)
        pygame.display.update()

pygame.quit()
