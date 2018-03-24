#!/home/g/anaconda3/bin/python

import sys
import numpy as np
import data

def main():
    if len(sys.argv) != 2:
        print('%s [datafile.csv]' % (sys.argv[0]))
        sys.exit(1)

    while True:
        try:
            var = input("Enter a mileage: ")
            var = int(var)
        except ValueError:
            print('You did not enter an valid integer...Please try again')
        except (EOFError, KeyboardInterrupt) as e:
            print('\nBye...')
            sys.exit()
        else:
            if var <= 0:
                print("A car can't have a negativ mileage, you fool !")
            elif var > 500000:
                print("Have you ever seen a car with %.f miles??!" % var)
            else:
                break

    dat = data.Data(sys.argv[1], ',')
    dat.set_thetas('.parameters')
    ret = dat.estimate_result(var)
    if ret < 0:
        ret = 0
    print('We estimate you car to %.f' % ret)

if __name__ == "__main__":
    main()
