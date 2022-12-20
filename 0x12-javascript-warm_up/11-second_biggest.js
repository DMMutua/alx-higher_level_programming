#!/usr/bin/node

//A Script that Searches for the Second Biggest Integer
//In A list of Arguments

if (process.argv.length <= 3)
{
  console.log(0);
}
else
{
  const array_of_args = process.argv.map(Number)
  .slice(2, process.argv.length)
  .sort((a, b) => b - a);
  console.log(array_of_args[1]);
}
