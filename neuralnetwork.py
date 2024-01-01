import pygame

from colors import RED, BLUE, LIGHTER_GRAY
from layer import Layer
from settings import SCREEN, BORDER


class NeuralNet:
    def __init__(self, layer_sizes):
        self.layers = self.create_layers(layer_sizes)

    @staticmethod
    def normalize_inputs(inputs):
        return inputs[0] / BORDER.width, inputs[1] / BORDER.height

    def get_outputs(self, inputs):
        if inputs[0] == 1000 and inputs[1] == 790:
            pass
        inputs = self.normalize_inputs(inputs)
        if self.layers[0].numInputs == len(inputs):
            for one_layer in self.layers:
                inputs = one_layer.get_layer_outputs(inputs)
        else:
            raise Exception("Incorrectly sized input for neural network")
        return inputs

    @staticmethod
    def create_layers(layer_sizes):
        """
        Creates layers according to layer sizes
        :param layer_sizes: List of integers defining the layer sizes
        :return: A List of Layers
        """
        layers = []
        # Loop through layers and add layer to layers list
        for i in range(len(layer_sizes) - 1):
            layers.append(Layer(layer_sizes[i], layer_sizes[i + 1]))
        return layers

    # Temp Functions
    def manual_set_weights(self, weights):  # Only when 2 inputs and 2 outputs
        i = 0
        for layer in self.layers:
            for weight in layer.weights:
                weight[0] = weights[i]
                i += 1
                weight[1] = weights[i]
                i += 1
                if i <= 6:
                    weight[2] = weights[i]
                    i += 1

    def manual_set_biases(self, biases):
        i = 0
        for layer in self.layers:
            layer.biases[0] = biases[i]
            i += 1
            layer.biases[1] = biases[i]
            i += 1
            if i <= 2:
                layer.biases[2] = biases[i]
                i += 1

    def classify(self, inputs):
        outputs = self.get_outputs(inputs)

        if outputs[0] > outputs[1]:
            return 0
        else:
            return 1
