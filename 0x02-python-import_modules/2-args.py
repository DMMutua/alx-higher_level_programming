#!/usr/bin/python3

import sys

if __name__ == "__main__":
    import sys
    """ Prints the argument list passed to the program
    
    Prints the number of arguments passed in the program first

    """

    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))

    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))

