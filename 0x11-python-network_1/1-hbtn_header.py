#!/usr/bin/python3
"""A Module with a script that sends a request to the URL given as Its first argument during command line execution.
Displays the value of the X-Request-Id Variable found in the header of response.
"""

from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    with urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
