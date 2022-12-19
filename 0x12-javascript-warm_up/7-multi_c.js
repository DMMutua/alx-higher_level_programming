#!/usr/bin/node

// Printing 'C is fun' for `x` number of times where `x`
// is the first argument passed to the script.

occurences = Math.floor(Number(process.argv[2]));
if typeof occurences != Number
{
  console.log("Missing number of occurrences");
}
else
{
  for (let i = 0; i < occurences; i++)
  {
    console.log('C is fun');
  }
}
