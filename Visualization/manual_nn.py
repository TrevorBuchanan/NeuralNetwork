import utility
from NeuralNet.neuralnetwork import NeuralNet
from Visualization.colors import TRANSPARENT_BLUE, TRANSPARENT_RED
from Visualization.settings import BORDER, SCREEN


class ManualNN:
    def __init__(self):
        self.NN = NeuralNet([2, 3, 2])

    def set_weights(self, weights):  # Only when 2 inputs and 2 outputs
        i = 0
        for layer in self.NN.layers:
            for weight in layer.weights:
                weight[0] = weights[i]
                i += 1
                weight[1] = weights[i]
                i += 1
                if i <= 6:
                    weight[2] = weights[i]
                    i += 1

    def set_biases(self, biases):
        i = 0
        for layer in self.NN.layers:
            layer.biases[0] = biases[i]
            i += 1
            layer.biases[1] = biases[i]
            i += 1
            if i <= 2:
                layer.biases[2] = biases[i]
                i += 1

    def classify(self, inputs):
        outputs = self.NN.get_outputs(inputs)

        if outputs[0] > outputs[1]:
            return 0
        else:
            return 1

    def visualize(self):
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
