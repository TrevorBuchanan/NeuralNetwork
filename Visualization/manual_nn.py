from NeuralNet.neuralnetwork import NeuralNet
from Visualization.nn_manager import NNManager


class ManualNN(NNManager):
    def __init__(self):
        super().__init__()
        self.NN = NeuralNet([2, 3, 2])

    def set_weights(self, weights):  # Only when 2 inputs and 2 outputs
        """
        Manually sets the weights of neural network
        :param weights: Float list of length 12
        """
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
        """
        Manually sets the biases of neural network
        :param biases: Float list of length 5
        """
        i = 0
        for layer in self.NN.layers:
            layer.biases[0] = biases[i]
            i += 1
            layer.biases[1] = biases[i]
            i += 1
            if i <= 2:
                layer.biases[2] = biases[i]
                i += 1
