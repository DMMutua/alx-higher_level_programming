#!/usr/bin/node

const first_arg = Math.floor(Number(process.argv[2]));

if (isNaN(first_arg)) {
  console.log('Not a number');
}
else {
   console.log('My number: ' + first_arg);
}

