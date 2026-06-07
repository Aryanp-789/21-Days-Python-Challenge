# Day 01 - Python Basics: Variables, Data Types, Input and Output

## Objective

The goal of Day 1 is to understand the basic building blocks of Python programming:

- What is Python?
- Variables
- Data Types
- Input and Output
- Simple Programs

---

## What is Python?

Python is a high-level, interpreted, and easy-to-learn programming language.

### Features of Python

- Easy syntax
- Beginner-friendly
- Open source
- Cross-platform
- Large community support
- Used in AI, Machine Learning, Data Science, Web Development, and Automation

---

## Installing Python

1. Download Python from https://www.python.org
2. Install Python.
3. Check installation using:

```bash
python --version
```

or

```bash
python3 --version
```

---

## First Python Program

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

---

## Variables

Variables are used to store data.

### Example

```python
name = "Aryan"
age = 21
```

Here:

- `name` stores text
- `age` stores a number

---

## Rules for Naming Variables

✅ Valid

```python
name = "Aryan"
student_age = 21
_marks = 95
```

❌ Invalid

```python
1name = "Aryan"
student-age = 21
class = "Python"
```

---

## Data Types

Python supports different data types.

### String (str)

```python
name = "Aryan"
```

### Integer (int)

```python
age = 21
```

### Float (float)

```python
cgpa = 8.5
```

### Boolean (bool)

```python
is_student = True
```

---

## Checking Data Types

```python
name = "Aryan"

print(type(name))
```

### Output

```text
<class 'str'>
```

---

## Output Function

The `print()` function is used to display information.

### Example

```python
print("Welcome to Python")
```

### Output

```text
Welcome to Python
```

---

## Input Function

The `input()` function is used to take input from the user.

### Example

```python
name = input("Enter your name: ")

print("Hello", name)
```

### Sample Output

```text
Enter your name: Aryan
Hello Aryan
```

---

## Type Conversion

Input values are treated as strings by default.

### Example

```python
age = int(input("Enter age: "))

print(age)
```

### Common Conversions

```python
int()
float()
str()
bool()
```

---

## Program 1: Personal Introduction

```python
name = input("Enter your name: ")
college = input("Enter your college: ")

print("Name:", name)
print("College:", college)
```

---

## Program 2: Add Two Numbers

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)
```

### Sample Output

```text
Enter first number: 10
Enter second number: 20
Sum = 30
```

---

## Program 3: Calculate Age After 5 Years

```python
age = int(input("Enter your current age: "))

future_age = age + 5

print("Your age after 5 years will be:", future_age)
```

---

## Key Learnings

- Python is simple and beginner-friendly.
- Variables store values.
- Different data types exist for different kinds of data.
- `print()` displays output.
- `input()` accepts user input.
- Type conversion helps convert data into required formats.

---

## Day 1 Summary

Today I learned:

✅ Python Basics

✅ Variables

✅ Data Types

✅ Input and Output

✅ Type Conversion

✅ Basic Python Programs

---

## Challenge Completed

- [x] Installed Python
- [x] Wrote Hello World Program
- [x] Practiced Variables
- [x] Practiced Data Types
- [x] Took User Input
- [x] Created Simple Programs

#21DaysPythonChallenge
