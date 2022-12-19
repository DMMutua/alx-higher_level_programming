#!/usr/bin/node

//A script that prints a square with the 'X' Letter

const sq_size = Math.floor(Number(process.argv[2]));

if (isNaN(sq_size))
{
  console.log('Missing size');
}
else
{
  let square_object = ''; // object to hold the square

  for (let i = 0; i < sq_size; i++)
  {
    for (let j = 0; j < sq_size; j++)
    {
      square_object += 'X';
    }
    square_object += '\n'; // Adding a newline after Each Row
  }

  console.log(square_object)
}
