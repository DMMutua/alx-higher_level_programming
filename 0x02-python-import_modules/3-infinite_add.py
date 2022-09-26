#!/usr/bin/python3
if __name__ == "__main__":
    """
    Adds all the arguments given in a list and gives the result
    assumes all the arguments are integers

    """
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])

    print("{}".format(result))

