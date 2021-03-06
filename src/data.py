# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/16 20:21:51 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/17 09:33:32 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

def normalize(x, min, max):
    return (x - min) / (max - min)

def denormalize(x, min, max):
    return x * (max - min) + min

class Data:

    def __init__(self, arg=None, delimiter=None, alpha=0.1, n_epoch=1000):
        if arg is not None and delimiter is not None:
            self.data = self.get_data(arg, delimiter)
            self.epur_data()
        self.theta0 = 0.0
        self.theta1 = 0.0
        self.alpha = alpha if alpha is not None and alpha > 0.0 else 0.1
        self.n_epoch = n_epoch if n_epoch is not None and n_epoch > 0 else 1000
        self.mse_curve = []

    def get_data(self, arg, delimiter):
        try:
            with open(arg, 'rt') as csvfile:
                base_data = csv.reader(csvfile, delimiter=delimiter)
                list_data = [x for x in base_data]
                return np.array(list_data)
        except Exception as e:
            print(e)
            sys.exit(1)

    def epur_data(self):
        self.label_1 = self.data[0, 0]
        self.label_2 = self.data[0, 1]
        self.data = self.data[1:, :]
        self.data = self.data.astype(int)
        self.x = self.data[:, 0]
        self.y = self.data[:, 1]

    def display(self):
        plt.scatter(self.x, self.y)
        plt.xlabel(self.label_1)
        plt.ylabel(self.label_2)
        plt.title("Price of a car according to its mileage")
        plt.show()

    def draw_line(self):
        line_values = [self.estimate_result(i) for i in self.x]
        plt.scatter(self.x, self.y)
        plt.xlabel(self.label_1)
        plt.ylabel(self.label_2)
        plt.plot(self.x, line_values, 'r')
        plt.title("Price of a car according to its mileage with learned curve")
        plt.show()

    def display_gradient_descent(self):
        x_values = np.arange(0, self.n_epoch)
        plt.title("Mean squarred error")
        plt.xlabel("Number of epoch")
        plt.ylabel("Error")
        plt.plot(x_values, self.mse_curve)
        plt.show()

    def feature_scaling(self):
        self.x_norm = normalize(self.x, self.x.min(), self.x.max())
        self.y_norm = normalize(self.y, self.y.min(), self.y.max())

    def estimate(self, x):
        return self.theta0 + x * self.theta1

    def estimate_result(self, mileage):
        if self.theta0 == 0 and self.theta1 == 0:
            return 0
        normed = normalize(mileage, self.x.min(), self.x.max())
        price_normed = self.estimate(normed)
        price = denormalize(price_normed, self.y.min(), self.y.max())
        return price

    def calc_sum(self):
        m = self.x_norm.shape[0]
        sum0 = 0
        sum1 = 0
        mse = 0
        for i in range(m):
            sum0 += self.estimate(self.x_norm[i]) - self.y_norm[i]
            sum1 += (self.estimate(self.x_norm[i]) - self.y_norm[i]) * self.x_norm[i]
            mse += (self.estimate(self.x_norm[i]) - self.y_norm[i]) ** 2
        return [sum0, sum1, mse]

    def gradient_descent(self):
        m = self.x_norm.shape[0]
        a = self.theta0
        b = self.theta1

        for i in range(self.n_epoch):
            sum0, sum1, mse = self.calc_sum()
            self.theta0 -= self.alpha * sum0 / m
            self.theta1 -= self.alpha * sum1 / m
            self.mse_curve.append(mse / m)

    def write_thetas(self):
        try:
            with open('.parameters', 'w') as file:
                file.write(str(self.theta0) + "\n")
                file.write(str(self.theta1) + "\n")
        except Exception as e:
            print(e)
            sys.exit(1)

    def set_thetas(self, file):
        try:
            with open(file, 'rt') as file:
                self.theta0 = float(file.readline())
                self.theta1 = float(file.readline())
        except FileNotFoundError:
            print('No learning parameters found, please run learning.py first')
        except Exception as e:
            print(e)

    def get_accuracy(self):
        accuracies = []
        for value in self.data:
            res = self.estimate_result(value[0])
            va = float(value[1])
            accuracies.append(abs(((va - res) / va) * 100))
        return (100 - (sum(accuracies) / len(accuracies)))