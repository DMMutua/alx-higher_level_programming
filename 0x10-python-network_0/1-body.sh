#!/bin/bash
# A script to Take In a URL, Send a `GET` Request, and Display the body only of 200 Status code.
curl -sL -o /dev/null -w "%{http_code}\n{url_effective}\n" $1 -f && echo $(curl -sL $1)
