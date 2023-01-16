#!/bin/bash
# Script to print the `Content-Length` value of cURLed URL.
curl -s -o /dev/null -w "%{size_download}" $1
