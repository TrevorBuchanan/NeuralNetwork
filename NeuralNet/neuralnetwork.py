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

    def cost(self, datapoint):
        """
        Get cost for a single datapoint
        :param datapoint: Input type of DataPoint holding inputs and expected outputs
        :return: accumulated cost from each node cost in the output layer
        """
        calculated_outputs = self.get_outputs(datapoint.inputs)
        output_layer = self.layers[-1]
        cost = 0
        for i, calc_out in enumerate(calculated_outputs):
            cost += output_layer.node_cost(calc_out, datapoint.expected_outputs[i])
        return cost

    # For manual network control the cost may not be an accurate depiction of how well data is classified
    # due to the decision logic of the classify function. If outputs are [1, 0.9], and desired output is
    # poisonous 1 or [1, 0], then there will be a total cost of 0.9 * 0.9 even though the output was "correct".
    def total_cost(self, data):
        """
        Get total cost for list of DataPoints
        :param data: List of DataPoints
        :return: Total cost for datapoints list
        """
        total_cost = 0
        for datapoint in data:
            total_cost += self.cost(datapoint)
        return total_cost / len(data)

    def apply_all_gradients(self, learn_rate):
        for layer in self.layers:
            layer.apply_gradients(learn_rate)

    def learn(self, training_data, learn_rate):
        h = 0.0001
        original_cost = self.total_cost(training_data)

        for layer in self.layers:
            for in_index in range(layer.numInputs):
                for out_index in range(layer.numOutputs):
                    layer.weights[in_index][out_index] += h
                    delta_cost = self.total_cost(training_data) - original_cost
                    layer.weights[in_index][out_index] -= h
                    layer.wGradients[in_index][out_index] = delta_cost / h

            for bias_index in range(len(layer.biases)):
                layer.biases[bias_index] += h
                delta_cost = self.total_cost(training_data) - original_cost
                layer.biases[bias_index] -= h
                layer.bGradients[bias_index] = delta_cost / h

        self.apply_all_gradients(learn_rate)
