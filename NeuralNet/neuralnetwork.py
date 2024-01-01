from NeuralNet.layer import Layer
from Visualization.settings import BORDER


class NeuralNet:

    def __init__(self, layer_sizes):
        self.layers = self.create_layers(layer_sizes)

    @staticmethod
    def normalize_inputs(inputs):
        """
        Normalizes input to workable range
        :param inputs: List of inputs
        :return: Normalized (scaled) inputs
        """
        # Modified for input size
        return inputs[0] / BORDER.width, inputs[1] / BORDER.height

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

    def get_outputs(self, inputs):
        """
        Runs inputs through all layers in the neural network
        :param inputs: List of inputs (Must be same size as first layer in the neural network)
        :return: List of outputs from neural network
        """
        inputs = self.normalize_inputs(inputs)
        if self.layers[0].numInputs == len(inputs):
            for one_layer in self.layers:
                inputs = one_layer.get_layer_outputs(inputs)
        else:
            raise Exception("Incorrectly sized input for neural network")
        return inputs
