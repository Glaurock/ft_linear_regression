#!/home/g/anaconda3/bin/python

import sys
import numpy as np
import data

def main():
    if len(sys.argv) != 2:
        print('Usage...')
        sys.exit(1)

    alpha = 0.1
    iter = 1000

    dat = data.Data(sys.argv[1], ',')
    dat.feature_scaling()
    dat.gradient_descent(alpha, iter)
    dat.write_thetas()

if __name__ == "__main__":
    main()
