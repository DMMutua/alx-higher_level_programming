#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    
    """ 
    Printing result of addition between two numbers 

    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
