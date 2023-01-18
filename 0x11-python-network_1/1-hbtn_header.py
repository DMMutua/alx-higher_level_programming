#!/usr/bin/python3
"""A Module with a script that sends a request to the URL given as Its first argument during command line execution.
Displays the value of the X-Request-Id Variable found in the header of response.
"""

from urllib.request import Request, urlopen
from sys import argv


if __name__ == '__main__':
    request = Request(argv[1])

    with urlopen(request) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
