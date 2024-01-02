from NeuralNet.neuralnetwork import NeuralNet
from Visualization.visualize_nn_manager import VisualizeNNManager


class AutoNN(VisualizeNNManager):
    def __init__(self, layer_sizes):
        super().__init__()
        self.NN = NeuralNet(layer_sizes)
