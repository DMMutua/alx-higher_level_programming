#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

if (isNaN(size) || !(process.argv[2])); {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; ++i) {
    for (let z = 0; z < size; ++z) {
      console.log('X');
    }
    console.log('\n');
  }
}
