# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    learning.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/16 20:21:53 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/17 09:29:56 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
import plac

import data

@plac.annotations(
    dataset = plac.Annotation("Dataset",'positional'),
    alpha = plac.Annotation('Set the learning rate', 'option', 'l', float),
    n_epoch = plac.Annotation('Set the number of epochs', 'option', 'e', int),
)
def learning(dataset, alpha, n_epoch):
    dat = data.Data(dataset, ',', alpha, n_epoch)
    dat.display()
    dat.feature_scaling()
    print("Starting to learn parameters...")
    dat.gradient_descent()
    dat.write_thetas()
    print("Parameters found and stored in file '.parameters'")
    dat.draw_line()
    dat.display_gradient_descent()

if __name__ == "__main__":
    plac.call(learning)
