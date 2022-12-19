#!/usr/bin/node

// Printing a Message Depending on Number of Arguments Passed.

const argument_count = process.argv.length;

if argument_count === 2;
{
  console.log("No Argument");
}
if argument_count === 3;
{
  console.log("Argument found");
}
else
{
  console.log("Arguments found");
}
