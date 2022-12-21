#!/usr/bin/node

const first_arg = process.argv[2];

if (process.argv[2]) {
  console.log(first_arg);
} else {
  console.log('No Argument');
}
