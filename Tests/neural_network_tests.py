import unittest

from NeuralNet.neuralnetwork import NeuralNet


class NeuralNetworkTests(unittest.TestCase):
    def test_get_outputs(self):
        inputs = [5, -2]
        test_nn = NeuralNet([2, 3, 2])
        weights1 = [[2, -2, -3], [4, 1, 0]]
        biases1 = [3, -4, 5]
        weights2 = [[7, -1], [3, 3], [-2, -6]]
        biases2 = [-2, 3]
        test_nn.layers[0].weights = weights1
        test_nn.layers[0].biases = biases1
        test_nn.layers[1].weights = weights2
        test_nn.layers[1].biases = biases2

        calc_out = test_nn.get_outputs(inputs)
        exp_out = [0.939005837737, 0.0206656219536]

        self.assertAlmostEqual(exp_out[0], calc_out[0], 5)
        self.assertAlmostEqual(exp_out[1], calc_out[1], 5)
