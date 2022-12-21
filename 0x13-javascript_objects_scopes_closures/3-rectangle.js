#!/usr/bin/node 

//Rectangle Class with Constructor and Method for Printing

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
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
};
