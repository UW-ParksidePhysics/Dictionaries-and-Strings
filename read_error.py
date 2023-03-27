# exercise 6.4
# using lnsum.txt
import numpy as np


def read_data(filename):
    infile = open(filename, 'r').readlines()[39:44]  # only care about lines 40-44 in the txt file
    # making empty arrays for the data from lnsum.txt
    epsilon_array = np.array([])
    error_array = np.array([])
    n_array = np.array([])
    for line in infile:
        words = line.split()
        epsilon = float(words[1][0]) * 10 ** float(words[1][-4:-1])  # really dumb way to work around scientific notation in the txt file
        epsilon_array = np.append(epsilon_array, epsilon)  # appends the values of epsilon to its empty array
        error = float(words[4][0:4]) * 10 ** float(words[4][-4:-1])
        error_array = np.append(error_array, error)
    return epsilon_array, error_array, n_array


print(read_data('lnsum.txt'))
