#!/home/g/anaconda3/bin/python

import sys
import numpy as np
import data

def main():
    if len(sys.argv) != 2:
        print('%s [datafile.csv]' % (sys.argv[0]))
        sys.exit(1)

    alpha = 0.1
    iter = 1000

    dat = data.Data(sys.argv[1], ',')
    dat.display()
    dat.feature_scaling()
    print("Starting to learn parameters...")
    dat.gradient_descent(alpha, iter)
    dat.write_thetas()
    print("Parameters found and stored in file .parameters")
    dat.draw_line()

if __name__ == "__main__":
    main()
