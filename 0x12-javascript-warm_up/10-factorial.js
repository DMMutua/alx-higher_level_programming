#!/usr/bin/node

// A Script that Uses a Factorial Fuction to Give the Factorials
// of Numbers passed as Arguments to the Script Itself.

function factorial(number)
{
  if (number === 0) || (isNaN(number))
  {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
