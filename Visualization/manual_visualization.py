import random

from pygame_widgets.slider import Slider

from NeuralNet.data_point import DataPoint
from Visualization import fruit
from Visualization.colors import DARK_GRAY, WHITE
from Visualization.manual_nn import ManualNN
from Visualization.settings import SCREEN, FONT, BORDER
from Visualization.visualization import Visualization


class ManualVisualization(Visualization):
    def __init__(self, num_fruits):
        super().__init__(num_fruits)
        self.NN_control = ManualNN()
        self.sliders = []
        self.create_sliders(17)

    def create_sliders(self, num_sliders):
        """
        Creates sliders
        :param num_sliders: Integer value of how many sliders to create
        """
        extra_space_indices = [5, 8, 14]
        initial_y = 40
        spacing = 20
        extra_space = 40
        for i in range(num_sliders):
            self.sliders.append(
                Slider(SCREEN, 10, initial_y, 70, 10, min=-25, max=25, step=0.1, initial=random.uniform(-25, 25)))
            initial_y += spacing
            if i in extra_space_indices:
                initial_y += extra_space

    def draw_visualization(self):
        # Fill background
        SCREEN.fill(DARK_GRAY)

        # Draw Grid
        self.graph.draw_grid("Spot Size", "Spike Length")

        # Draw fruits
        fruit.draw_fruits(self.fruits)

        # Draw NN visualization
        self.NN_control.visualize()

        # Get weights and biases from sliders and set the corresponding weights and biases in the neural network
        self.NN_control.set_weights([self.sliders[0].value, self.sliders[1].value, self.sliders[2].value,
                                    self.sliders[3].value, self.sliders[4].value, self.sliders[5].value,
                                    self.sliders[9].value, self.sliders[10].value, self.sliders[11].value,
                                    self.sliders[12].value, self.sliders[13].value, self.sliders[14].value])
        self.NN_control.set_biases(
            [self.sliders[6].value, self.sliders[7].value, self.sliders[8].value, self.sliders[15].value,
             self.sliders[16].value])

        # Weight and bias labels
        text = FONT.render("Weights", True, WHITE)
        SCREEN.blit(text, [10, 10])
        text = FONT.render("Biases", True, WHITE)
        SCREEN.blit(text, [10, 170])
        text = FONT.render("Weights", True, WHITE)
        SCREEN.blit(text, [10, 270])
        text = FONT.render("Biases", True, WHITE)
        SCREEN.blit(text, [10, 430])

        cost = round(self.get_cost(), 3)
        text = FONT.render(f"Cost: {cost}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 150, BORDER.height - 70])

        correct = self.get_correct()
        text = FONT.render(f"Correct: {correct}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 150, BORDER.height - 40])
