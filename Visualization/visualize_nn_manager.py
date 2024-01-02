import utility
from NeuralNet.neuralnetwork import NeuralNet
from Visualization.colors import TRANSPARENT_BLUE, TRANSPARENT_RED
from Visualization.settings import BORDER, SCREEN


class VisualizeNNManager:
    def __init__(self):
        self.NN = NeuralNet([1, 1])  # Default network layers: 1 -> 1

    def classify(self, inputs):
        """
        Runs input though network and classifies fruit (given position) as poisonous 1 or safe 0
        :param inputs: 2D position i.e. a tuple or list of length 2
        :return: 1 if poisonous, 0 if safe
        """
        outputs = self.NN.get_outputs(inputs)

        if outputs[0] > outputs[1]:
            return 1
        else:
            return 0

    def visualize(self):
        """
        Runs through points on screen and draws a point with color according to classification
        """
        x = 0
        while 0 <= x <= BORDER.width:
            y = 0
            while 0 <= y <= BORDER.height:
                if self.classify((x, y)):  # classified as 1 so poisonous
                    utility.draw_circle_alpha(SCREEN, TRANSPARENT_RED, (x, y), 3)
                else:  # classified as 0 so safe
                    utility.draw_circle_alpha(SCREEN, TRANSPARENT_BLUE, (x, y), 3)
                y += 10
            x += 10
