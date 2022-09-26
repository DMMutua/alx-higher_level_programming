#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in matrix:
            i = 1
            length = len(rows)

            for column in rows:
                if i == length:
                    print('{:d}'.format(column), end='')
                else:
                    print('{:d}'.format(column), end=' ')
                i += 1

            print()
