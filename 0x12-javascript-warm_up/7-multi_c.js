#!/usr/bin/node

const occurences = Number(process.argv[2]);

if (isNaN(occurences) || !(process.argv[2])) {
  console.log('Missing Number of occurrences');
} else {
  for (let i = 0; i < occurences; ++i) {
    console.log('C is fun');
}
