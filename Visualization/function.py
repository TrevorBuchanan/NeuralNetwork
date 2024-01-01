import pygame

import utility
from Visualization.colors import WHITE, LIGHTER_GRAY
from Visualization.settings import SCREEN, BORDER


class Function:
    def __init__(self, xy_offsets):
        self.points = []
        self.points_dict = {}
        self.XY_offsets = xy_offsets

    def graph_func(self):
        for i in range(len(self.points)):
            if i + 1 != len(self.points):
                pygame.draw.line(SCREEN, LIGHTER_GRAY, self.points[i], self.points[i + 1], 5)

    def linear_func_points(self, m, b):
        m = -1 * m
        x = 0
        y = self.XY_offsets[1] - b
        points = []
        while 0 <= x <= BORDER.width:
            points.append((x, y))
            x += 1
            y += m

        self.points_dict = utility.tup_list_to_dict(points)
        return points
