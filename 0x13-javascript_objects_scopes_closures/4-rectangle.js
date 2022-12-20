#!/usr/bin/node

// Checks for Rectangle parameters

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rows = '';
      for (let j = 0; j < this.width; j++) {
        rows += 'X';
    }
      console.log(row);
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

