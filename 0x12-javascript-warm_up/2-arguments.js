#!/usr/bin/node

// Printing a Message Depending on Number of Arguments Passed.

const argument_count = process.argv.length;

console.log(argument_count === 2 ? 'No Argument' : count === 3 ?
'Argument Found' : 'Arguments found');
