import math
import unittest

from NeuralNet.layer import Layer


class LayerTests(unittest.TestCase):
    def test_get_layer_outputs(self):
        inputs = [2, -1]
        test_layer = Layer(2, 2)
        calc_out = test_layer.get_layer_outputs(inputs)

        output1 = inputs[0] * test_layer.weights[0][0] + inputs[1] * test_layer.weights[1][0] + test_layer.biases[0]
        output2 = inputs[0] * test_layer.weights[0][1] + inputs[1] * test_layer.weights[1][1] + test_layer.biases[1]
        exp_out = (1 / (1 + (math.e ** -output1)), 1 / (1 + (math.e ** -output2)))

        print(calc_out)
        self.assertAlmostEqual(exp_out[0], calc_out[0], 5)
        self.assertAlmostEqual(exp_out[1], calc_out[1], 5)
