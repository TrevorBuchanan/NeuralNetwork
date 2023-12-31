import pygame

from colors import RED, BLUE
from layer import Layer
from settings import SCREEN, BORDER


def create_layers(layer_sizes):
    # # Initializes the first layer of NN according to input
    # layers = [Layer(inputs, layer_sizes[0])]

    layers = []
    # Initializes the rest of the nodes in the NN to 0
    for i in range(len(layer_sizes) - 1):
        new_inputs = [0 for _ in range(layer_sizes[i])]
        layers.append(Layer(new_inputs, layer_sizes[i + 1]))
    return layers


class NeuralNet:
    def __init__(self, layer_sizes):
        self.layers = create_layers(layer_sizes)

    # Temp Functions
    def manual_set_weights(self, weights):  # Only when 2 inputs and 2 outputs
        i = 0
        for layer in self.layers:
            for weight in layer.weights:
                weight[0] = weights[i]
                i += 1
                weight[1] = weights[i]
                i += 1

    def manual_set_biases(self, biases):
        for layer in self.layers:
            layer.biases[0] = biases[0]
            layer.biases[1] = biases[1]

    def classify(self, inputs):
        if len(self.layers[0].inputs) == len(inputs):
            self.layers[0].inputs = inputs
        else:
            raise Exception("Incorrectly sized input for neural network")

        for one_layer in self.layers:
            inputs = one_layer.get_outputs(inputs)
        outputs = inputs

        if outputs[0] > outputs[1]:
            return 1
        else:
            return 0

    def get_decision_boundary(self):
        points = []
        for x in range(0, BORDER.width, 10):
            for y in range(0, BORDER.height, 1):
                if self.classify((x, y)) != self.classify((x, y + 1)):
                    points.append((x, y))
        print()
        return points
