#!/usr/bin/node

function factorial(num) {
  return (num * (factorial(num - 1)));
}

const arg = Math.floor(Number(process.argv[2]));

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
