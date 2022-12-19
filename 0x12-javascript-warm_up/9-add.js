#!/usr/bin/node

// A Script with a function that Adds two Integers Given as Arguments to
// it when it Initiates.

function add(a, b)
{
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
