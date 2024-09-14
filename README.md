Here is the revised README file with the correct author name:

---

# 0x08. Python - More Classes and Objects

## Description
This repository contains tasks and solutions for Python projects related to classes and objects, focusing on object-oriented programming. It builds upon foundational concepts like encapsulation, inheritance, and polymorphism, with an emphasis on writing clean, modular code for various tasks involving rectangles and more advanced use cases such as backtracking with the N Queens problem.

---

### Tasks

#### 0. **Simple Rectangle**
- **File:** `0-rectangle.py`
- This task defines an empty class `Rectangle`. The class does not include any attributes or methods.

#### 1. **Real Definition of a Rectangle**
- **File:** `1-rectangle.py`
- Defines a class `Rectangle` with private attributes `width` and `height`, including property methods to set and retrieve them. It also includes validation to ensure the attributes are integers and non-negative.

#### 2. **Area and Perimeter**
- **File:** `2-rectangle.py`
- The class `Rectangle` is extended with public instance methods to calculate the area and perimeter of the rectangle.

#### 3. **String Representation**
- **File:** `3-rectangle.py`
- Adds a method to return a string representation of the rectangle using the `#` character. If either width or height is 0, the string will be empty.

#### 4. **Eval is Magic**
- **File:** `4-rectangle.py`
- The `__repr__` method is added to the `Rectangle` class to allow a rectangle object to be recreated by passing the string representation to `eval()`.

#### 5. **Detect Instance Deletion**
- **File:** `5-rectangle.py`
- This task introduces a destructor `__del__` method that prints "Bye rectangle..." whenever an instance of the class is deleted.

#### 6. **How Many Instances**
- **File:** `6-rectangle.py`
- A class attribute `number_of_instances` is added to the `Rectangle` class, which keeps track of how many instances have been created or deleted.

#### 7. **Change Representation**
- **File:** `7-rectangle.py`
- The `print_symbol` class attribute is introduced to allow for customizing the symbol used when printing the rectangle. It can be set to any type.

#### 8. **Compare Rectangles**
- **File:** `8-rectangle.py`
- A static method `bigger_or_equal` is introduced to compare two rectangles by their area and return the bigger one.

#### 9. **A Square is a Rectangle**
- **File:** `9-rectangle.py`
- A class method `square` is introduced to create a new `Rectangle` instance where `width` and `height` are equal.

#### 10. **N Queens**
- **File:** `101-nqueens.py`
- Implements a program to solve the N Queens puzzle, placing N non-attacking queens on an N×N chessboard. The program prints every possible solution for a given board size N.

---

## Author
**Sara Elkomy**

---

You can place this in the `README.md` file for your project. Let me know if you'd like any further changes!
