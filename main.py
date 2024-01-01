import pygame

from Visualization.settings import FPS
from Visualization.manual_visualization import ManualVisualization


if __name__ == '__main__':
    clock = pygame.time.Clock()

    manual_visualization = ManualVisualization(200)

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

        manual_visualization.draw_visualization(events)

        pygame.display.update()

pygame.quit()
