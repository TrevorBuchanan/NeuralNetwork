import pygame

from Visualization.colors import WHITE, LIGHT_GRAY, GRAY
from Visualization.settings import SCREEN, BORDER, FONT


class Graph:
    def __init__(self, line_scale):
        """
        :param line_scale: Scales the number of lines in the graph (int)
        """
        self.line_scale = line_scale
        self.XY_offsets = self.get_offsets()

    def get_offsets(self):
        """
        :return: x-axis offset and y-axis offset as a tuple
        """
        h_spacing = BORDER.height / self.line_scale
        v_spacing = BORDER.width / self.line_scale / 2
        return h_spacing, BORDER.height - v_spacing

    def draw_grid(self, x_axis_name, y_axis_name):
        """
        Draws positive grid (graph with only quadrant 1)
        :param x_axis_name: Name of x-axis (string)
        :param y_axis_name: Name of y-axis (string)
        """
        h_spacing = BORDER.height / self.line_scale
        v_spacing = BORDER.width / self.line_scale / 2
        h = h_spacing
        v = BORDER.height - v_spacing

        # Horizontal lines
        while v >= 0:
            if v == BORDER.height - v_spacing:
                pygame.draw.line(SCREEN, LIGHT_GRAY, (0, v), (BORDER.width, v), 4)  # x-axis
            else:
                pygame.draw.line(SCREEN, LIGHT_GRAY, (0, v), (BORDER.width, v))
            v -= v_spacing

        # Vertical lines
        while h <= BORDER.width:
            if h == h_spacing:
                pygame.draw.line(SCREEN, LIGHT_GRAY, (h, 0), (h, BORDER.height), 4)  # y-axis
            else:
                pygame.draw.line(SCREEN, LIGHT_GRAY, (h, 0), (h, BORDER.height))
            h += h_spacing

        # Axis names
        text = FONT.render(x_axis_name, True, GRAY)
        text = pygame.transform.rotate(text, 90)
        SCREEN.blit(text, [int(h_spacing / 2), BORDER.height - 110 - v_spacing])

        text = FONT.render(y_axis_name, True, GRAY)
        SCREEN.blit(text, [h_spacing + 10, BORDER.height - int(h_spacing / 2) - 10])
