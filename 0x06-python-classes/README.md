# Classes and Objects In Python: Object Oriented Programming

## Learning Objectives
* Why Python programming is awesome
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the __dict__ of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

## Tasks

### 0. My first square
An empty class `Square` that defines a square

### 1. Square with size
A Class `Square` that defines a square by: (based on `0-square.py`)
* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

### 2. Size validation
Write a class Square that defines a square by: (based on `1-square.py`)

* Private instance attribute: `size`
* Instantiation with optional size: def __init__(self, size=0):
* size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

### 3. Area of a square
Write a class `Square` that defines a square by: (based on `2-square.py`)
* Private instance attribute: size
* Instantiation with optional `size`: `def __init__(self, size=0):`
	* size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
	* if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module.

### 4. Access and update private attribute
### 5. Printing a square
### 6. Coordinates of a square
### 7. Singly linked list
### 8. Print Square instance
### 9. Compare 2 squares
### 10.ByteCode -> Python #5

