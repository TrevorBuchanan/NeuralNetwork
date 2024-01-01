from NeuralNet.neuralnetwork import NeuralNet
from Visualization.nn_manager import NNManager


class AutoNN(NNManager):
    def __init__(self, layer_sizes):
        super().__init__()
        self.NN = NeuralNet(layer_sizes)
