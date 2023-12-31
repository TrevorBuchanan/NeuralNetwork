# import numpy as np
import math


def activation_function(weighted_input):
    return weighted_input
    # return 1 / (1 + (math.e ** -weighted_input))


class Layer:
    def __init__(self, inputs, output_amount):
        self.inputs = inputs

        self.numInputs = len(inputs)
        self.numOutputs = output_amount

        # self.weights = np.random.rand(input_amount, output_amount)
        self.weights = [[1 for _ in range(output_amount)] for _ in range(self.numInputs)]
        # self.biases = np.random.rand(output_amount)
        # self.biases = np.zeros(output_amount)
        self.biases = [0 for _ in range(output_amount)]


    # Compute outputs
    def get_outputs(self, inputs):
        activations = [0 for _ in range(self.numOutputs)]
        for out_index in range(self.numOutputs):
            weighted_input = self.biases[out_index]
            for in_index in range(self.numInputs):
                weighted_input += inputs[in_index] * self.weights[in_index][out_index]
            activations[out_index] = activation_function(weighted_input)

        return activations
