import utility
from NeuralNet.neuralnetwork import NeuralNet
from Visualization.colors import TRANSPARENT_BLUE, TRANSPARENT_RED
from Visualization.settings import BORDER, SCREEN


class NNManager:
    def __init__(self):
        self.NN = NeuralNet([1, 1])  # Default network layers: 1 -> 1

    def classify(self, inputs):
        """
        Runs input though network and classifies fruit (given position) as poisonous 0 or safe 1
        :param inputs: 2D position i.e. a tuple or list of length 2
        :return: 0 if poisonous, 1 if safe
        """
        outputs = self.NN.get_outputs(inputs)

        if outputs[0] > outputs[1]:
            return 0
        else:
            return 1

    def visualize(self):
        """
        Runs through points on screen and draws a point with color according to classification
        """
        x = 0
        while 0 <= x <= BORDER.width:
            y = 0
            while 0 <= y <= BORDER.height:
                if self.classify((x, y)):
                    utility.draw_circle_alpha(SCREEN, TRANSPARENT_BLUE, (x, y), 3)
                else:
                    utility.draw_circle_alpha(SCREEN, TRANSPARENT_RED, (x, y), 3)
                y += 10
            x += 10
