#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat_elems = [n for row in matrix for n in row]
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print('{:d}'.format(row[i]), end=' ')
            else:
                print('{:d}'.format(row[i]), end='')
        print()
