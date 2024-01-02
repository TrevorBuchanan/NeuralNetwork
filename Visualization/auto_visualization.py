from Visualization import fruit
from Visualization.auto_nn import AutoNN
from Visualization.colors import DARK_GRAY, WHITE
from Visualization.settings import SCREEN, FONT, BORDER
from Visualization.visualization import Visualization


class AutoVisualization(Visualization):
    def __init__(self, num_fruits, layer_sizes):
        super().__init__(num_fruits)
        self.NN_control = AutoNN(layer_sizes)

    def draw_visualization(self):
        # Fill background
        SCREEN.fill(DARK_GRAY)

        # Draw Grid
        self.graph.draw_grid("Spot Size", "Spike Length")

        # Draw fruits
        fruit.draw_fruits(self.fruits)

        # Draw NN visualization
        self.NN_control.visualize()

        # Draw NN cost
        cost = round(self.get_cost(), 3)
        text = FONT.render(f"Cost: {cost}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 150, BORDER.height - 70])

        # Draw number of correctly classified fruits
        correct = self.get_correct()
        text = FONT.render(f"Correct: {correct}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 150, BORDER.height - 40])

        # NN learn
        self.NN_control.NN.learn(self.training_data, 0.5)
