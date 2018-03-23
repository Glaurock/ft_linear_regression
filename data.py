import numpy as np
import matplotlib.pyplot as plt
import csv

class Data():

    def __init__(self, arg, delimiter):
        self.data = self.get_data(arg, delimiter)
        self.label_1 = ""
        self.label_2 = ""
        self.theta = np.array([0.0, 0.0])
        self.x = 0
        self.y = 0

    def get_data(self, arg, delimiter):
        with open(arg, 'rt') as csvfile:
            base_data = csv.reader(csvfile, delimiter=delimiter)
            list_data = [x for x in base_data]
            return np.array(list_data)

    def epur_data(self):
        #self.label_1 = self.data[0, 0]
        #self.label_2 = self.data[0, 1]
        #self.data = self.data[1:, :]
        self.data = self.data.astype(int)
        self.x = self.data[:, [0, 1]]
        self.y = self.data[:, 2]

    def display(self):
        fig = plt.figure()
        ax = plt.axes()
        ax.scatter(self.x, self.y)
        plt.xlabel(self.label_1)
        plt.ylabel(self.label_2)
        plt.show()

    def estimate(self, x, theta):
        return theta[0] + theta[1] * x

    def cost_function(self, X, y, theta):
        m = X.shape[0]
        X = np.c_[np.ones(m), X]
        J = 0

        errors = pow((X.dot(theta) - y), 2)
        J = 1 / (2 * m) * sum(errors);
        return J

    def gradient_descent(self, X, y, theta, alpha, iter):
        m = X.shape[0]
        X = np.c_[np.ones(m), X]

        for i in range(iter):
            h = X.dot(theta)
            errors = h - y
            delta = X.transpose().dot(errors)
            theta = theta - (alpha / m) * delta

        return theta

    def feature_normalize(self, X):
        sigma = X.std()
        mu = X.mean()

        X_norm = (X - mu) / sigma
        return X_norm
