import numpy as np

class perceptron():
    def __init__(self, x, y, threshold = 0.5, learning_rate = 0.1, max_epochs = 10):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.x = x
        self.y = y
        self.max_epochs = max_epochs

    def initialize(self, init_type = 'zeros'):
        if init_type == 'random':
            self.weights = np.random.rand(len(self.x[0])) * 0.05
        if init_type == 'zeros':
            self.weights = np.zeros(len(self.x[0]))

    def train(self):
        epoch = 0
        while True:
            error_count = 0
            epoch += 1
            for (x,y) in zip(self.x, self.y):
                error_count += self.train_observation(x, y, error_count)
            if error_count == 0:
                print("training successful")
                break
            if epoch >= self.max_epochs:
                print("reached maximum epochs, no perfect prediction")
                break

    def train_observation(self, x, y, error_count):
        result = np.dot(x, self.weights) > self.threshold
        error = y - result
        if error != 0:
            error_count += 1
            for index, value in enumerate(x):
                self.weights[index] += self.learning_rate * error * value
        return error_count

    def predict(self, x):
        print("self.weights = {}, x = {}, np.dot(x, self.weights) = {}".format(self.weights, x, np.dot(x, self.weights)))
        return int(np.dot(x, self.weights) > self.threshold)

x = [(1,0,0),(1,1,0),(1,1,1),(1,1,1),(1,0,1),(1,0,1)]
y = [1,1,0,0,1,1]
p = perceptron(x,y)
p.initialize()
p.train()

print(p.predict((1,1,1)))
print(p.predict((1,0,1)))
