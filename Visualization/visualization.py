from Visualization.fruit import Fruit
from Visualization.function import Function
from Visualization.graph import Graph


class Visualization:
    def __init__(self, num_fruits):
        self.graph = Graph(9)
        self.fruit_function = Function(self.graph.XY_offsets)
        self.fruit_function.points = self.fruit_function.linear_func_points(-1 / 2, 500)
        self.fruits = [Fruit(self.fruit_function.points_dict) for _ in range(num_fruits)]

    def draw_visualization(self):
        """
        Draws a visualization of neural network
        """
        raise NotImplementedError
