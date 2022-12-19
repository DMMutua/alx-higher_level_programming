#!/usr/bin/node

// Converting the First Argument to Integer, If it Can Be Done.

const number = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My Number: ${number}`);
