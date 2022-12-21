#!/usr/bin/node

//A New Square Class That Inherits from The `Rectangle` Class.

const Rectangle = require('./4-rectangle'); // Importation

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  };

  double () {
    super.double();
  };

  print () {
    super.print();
  };
};
