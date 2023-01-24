#!/usr/bin/python3
"""A Module with a script that sends a request to the URL given as Its first argument during command line execution.
Displays the value of the X-Request-Id Variable found in the header of response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
