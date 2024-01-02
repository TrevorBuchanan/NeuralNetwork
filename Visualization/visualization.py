from NeuralNet.data_point import DataPoint
from Visualization.fruit import Fruit
from Visualization.function import Function
from Visualization.graph import Graph
from Visualization.visualize_nn_manager import VisualizeNNManager


class Visualization:
    def __init__(self, num_fruits):
        self.NN_control = VisualizeNNManager()
        self.graph = Graph(9)
        self.fruit_function = Function(self.graph.XY_offsets)
        self.fruit_function.points = self.fruit_function.linear_func_points(-1 / 2, 500)
        self.fruits = [Fruit(self.fruit_function.points_dict) for _ in range(num_fruits)]
        self.training_data = self.make_training_data(self.fruits)


    def draw_visualization(self):
        """
        Draws a visualization of neural network
        """
        raise NotImplementedError

    @staticmethod
    def make_training_data(fruits):
        data = []
        for f in fruits:
            if f.poisonous:
                dp = DataPoint(f.position, (1, 0))
            else:
                dp = DataPoint(f.position, (0, 1))
            data.append(dp)
        return data

    def get_cost(self):
        return self.NN_control.NN.total_cost(self.training_data)

    def get_correct(self):  # Refactor
        total = 0
        for f in self.fruits:
            if self.NN_control.classify(f.position) == f.poisonous:
                total += 1
        return total
