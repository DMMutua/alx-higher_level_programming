#!/bin/bash
# A script to Take In a URL, Send a `GET` Request, and Display the body only of 200 Status code.
resp=$(curl -so /dev/null -w "%{http_code}" -s $1 && echo $(curl -s $1))
