#!/usr/bin/node

array_of_ints = process.argv.slice(2);
array_of_ints = array_of_ints.sort((a, b) => b - a);

console.log(array_of_ints[1]);
