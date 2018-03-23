#!/home/g/anaconda3/bin/python

import sys
import data

import numpy as np

def main():
    if len(sys.argv) != 2:
        print('Usage...')
        exit(1)

    dat = data.Data(sys.argv[1], ',')
    dat.epur_data()
    #X = dat.feature_normalize(dat.x)
    #dat.display()
    #print(dat.cost_function(dat.x, dat.y, dat.theta))
    #theta = np.array([-1, 2])
    #print(dat.cost_function(dat.x, dat.y, theta))
    #print(X)
    #theta = dat.gradient_descent(X, dat.y, dat.theta, 0.01, 1500)
    #print(theta)
    #print(dat.estimate(100000, theta))


if __name__ == "__main__":
    main()
