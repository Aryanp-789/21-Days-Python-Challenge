# Day 7 - Functions in Python

## Introduction

Functions are one of the most important concepts in Python programming. A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we can create a function and use it whenever needed.

Functions make programs:
- Easier to read
- Easier to maintain
- More organized
- Less repetitive

---

## Why Use Functions?

Imagine you need to display a welcome message 20 times in your program.

Without functions, you would write the same code repeatedly.

With functions, you write the code once and call it whenever needed.

This saves time and makes the program cleaner.

---

## Creating a Function

In Python, functions are created using the `def` keyword.

### Syntax

```python
def function_name():
    # code block
```

### Example

```python
def greet():
    print("Hello Aryan!")

greet()
```

### Output

```
Hello Aryan!
```

---

## Function with Parameters

Parameters allow us to pass data into a function.

### Example

```python
def greet(name):
    print("Hello", name)

greet("Aryan")
```

### Output

```
Hello Aryan
```

---

## Function with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 5)
```

### Output

```
15
```

---

## Return Statement

The `return` keyword is used to send a value back from a function.

### Example

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
```

### Output

```
20
```

---

## Types of Functions

### 1. Built-in Functions

Python already provides many functions.

Examples:

```python
print()
len()
type()
input()
max()
min()
sum()
```

### Example

```python
numbers = [10, 20, 30]
print(len(numbers))
```

Output:

```
3
```

---

### 2. User-defined Functions

Functions created by programmers.

Example:

```python
def welcome():
    print("Welcome to Python")

welcome()
```

---

## Benefits of Functions

- Reusability
- Better code organization
- Easier debugging
- Reduced code duplication
- Improved readability

---

## Complete Example

```python
def add(a, b):
    return a + b

def square(num):
    return num * num

def greet(name):
    print("Hello,", name)

print("Addition:", add(10, 5))
print("Square:", square(6))
greet("Aryan")
```

### Output

```
Addition: 15
Square: 36
Hello, Aryan
```

---

## Day 7 Practice Questions

### Easy

1. Create a function to print your name.
2. Create a function to add two numbers.
3. Create a function to find the square of a number.

### Medium

4. Create a function to calculate the area of a rectangle.
5. Create a function to check whether a number is even or odd.
6. Create a function to find the largest of two numbers.

### Challenge

Create a simple calculator using functions for:

- Addition
- Subtraction
- Multiplication
- Division

---

## What I Learned Today

- What functions are
- Why functions are useful
- How to create functions
- How to pass parameters
- How to return values
- Difference between built-in and user-defined functions

---

## Day 7 Status

✅ Completed Day 7 of the 21-Day Python Challenge

### Topics Covered

- Functions
- Parameters
- Arguments
- Return Statement
- Code Reusability

---

### Author

Aryan Patil

21-Day Python Challenge 🚀
