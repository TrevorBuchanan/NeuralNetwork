from Visualization import fruit
from Visualization.auto_nn import AutoNN
from Visualization.colors import DARK_GRAY
from Visualization.settings import SCREEN
from Visualization.visualization import Visualization


class AutoVisualization(Visualization):
    def __init__(self, num_fruits, layer_sizes):
        super().__init__(num_fruits)
        self.NN = AutoNN(layer_sizes)

    def draw_visualization(self):
        # Fill background
        SCREEN.fill(DARK_GRAY)

        # Draw Grid
        self.graph.draw_grid("Spot Size", "Spike Length")

        # Draw fruits
        fruit.draw_fruits(self.fruits)

        # Draw NN visualization
        self.NN.visualize()
