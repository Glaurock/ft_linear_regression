# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    learning.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/16 20:21:53 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/17 09:21:15 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np

import data

def learning():
    if len(sys.argv) != 2:
        print('%s [datafile.csv]' % (sys.argv[0]))
        sys.exit(1)

    dat = data.Data(sys.argv[1], ',')
    dat.display()
    dat.feature_scaling()
    print("Starting to learn parameters...")
    dat.gradient_descent()
    dat.write_thetas()
    print("Parameters found and stored in file '.parameters'")
    dat.draw_line()
    dat.display_gradient_descent()

if __name__ == "__main__":
    learning()
