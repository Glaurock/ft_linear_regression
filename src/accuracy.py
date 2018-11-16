# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    accuracy.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/16 20:30:17 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/16 20:43:48 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np

import data

def predict():
    if len(sys.argv) != 2:
        print('%s [datafile.csv]' % (sys.argv[0]))
        sys.exit(1)

    dat = data.Data(sys.argv[1], ',')
    dat.set_thetas('.parameters')
    acc = dat.get_accuracy()
    print("The accuracy of this linear regression is: {:.2f}%".format(acc))


if __name__ == "__main__":
    predict()
