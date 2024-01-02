import math
import random


def activation_function(weighted_input):
    if weighted_input > 500:
        return 1
    if weighted_input < -500:
        return 0

    return 1 / (1 + (math.e ** -weighted_input))


class Layer:
    def __init__(self, input_amount, output_amount):
        self.numInputs = input_amount
        self.numOutputs = output_amount

        self.weights = [[random.uniform(-1, 1) / input_amount ** 0.5 for _ in range(output_amount)] for _ in
                        range(input_amount)]
        self.wGradients = [[0 for _ in range(output_amount)] for _ in range(input_amount)]

        self.biases = [0 for _ in range(output_amount)]
        self.bGradients = [0 for _ in range(output_amount)]

    @staticmethod
    def node_cost(calculated, expected):
        error = calculated - expected
        return error * error

    def get_layer_outputs(self, inputs):
        """
        Get list of outputs after running inputs through weights and biases in layer
        :param inputs: List (of length self.input_amount) of numbers
        :return: List of output numbers having run through layer and activation function
        """
        activations = [0 for _ in range(self.numOutputs)]
        for out_index in range(self.numOutputs):
            weighted_input = self.biases[out_index]
            for in_index in range(self.numInputs):
                weighted_input += inputs[in_index] * self.weights[in_index][out_index]
            activations[out_index] = activation_function(weighted_input)

        return activations

    def apply_gradients(self, learn_rate):  # NOT FINAL
        for out_index in range(self.numOutputs):
            self.biases[out_index] -= self.bGradients[out_index] * learn_rate
            for in_index in range(self.numInputs):
                # Why set equal to
                self.weights[in_index][out_index] -= self.wGradients[in_index][out_index] * learn_rate

        self.wGradients = [[0 for _ in range(self.numOutputs)] for _ in range(self.numInputs)]
        self.bGradients = [0 for _ in range(self.numOutputs)]
