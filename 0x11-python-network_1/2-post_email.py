#!/usr/bin/python3
"""
Sending a `POST` requewst to the passed URL with the email as a parameter.
displays the body of the response decoded in `utf-8`.
    Usage: ./2-post_email.py <URL> <email>
"""


import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email: sys.argv[2]"}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
