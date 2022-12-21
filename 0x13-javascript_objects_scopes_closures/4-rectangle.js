#!/usr/bin/node

// Rectangle Class with Methods for Constructing, Printing, 
// Rotating and Doubling the Rectangle Objects

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  };

  print () {
    for (let i = 0; i < this.height; i++) {
      let rows = '';
      for (let j = 0; j < this.width; j++) {
        rows += 'X';
    }
      console.log(rows);
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  };

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

