#!/bin/bash
# Script to print the `Content-Length` value of cURLed URL.
curl -sI $1 | grep -i "Content-Length" | cut -d' ' -f2
