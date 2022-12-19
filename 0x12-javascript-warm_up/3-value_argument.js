#!/usr/bin/node

// A Script that Prnts the First Argument Passed to It.

const first_script_argument = process.argv[2];

console.log(typeof first_script_argument === 'undefined' ? 'No argument' : first_script_argument)
