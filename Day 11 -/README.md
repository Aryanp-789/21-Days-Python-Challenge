# 🐍 Day 11 - Object-Oriented Programming (OOP) | 21 Days Python Challenge

Welcome to **Day 11** of my **21 Days Python Challenge**.

Today, I learned the fundamentals of **Object-Oriented Programming (OOP)** in Python. OOP is a programming paradigm that helps organize code into reusable, scalable, and maintainable objects. It is widely used in software development, web applications, game development, and many other real-world projects.

---

# 📚 Topics Covered

## 1. Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming approach based on the concept of **objects**. Objects contain both **data (attributes)** and **functions (methods)**.

### Advantages of OOP
- Code Reusability
- Better Code Organization
- Easy Maintenance
- Improved Security
- Scalability

---

## 2. Classes and Objects

A **Class** is a blueprint for creating objects.

An **Object** is an instance of a class.

Example:

```python
class Student:
    pass

student1 = Student()
```

---

## 3. Constructors (`__init__`)

A constructor is a special method that is automatically called when an object is created.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Aryan", 21)
```

---

## 4. Instance Variables

Instance variables store data specific to each object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## 5. Methods

Methods define the behavior of an object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")
```

---

## 6. Inheritance

Inheritance allows one class to inherit the properties and methods of another class.

Example:

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

---

## 7. Polymorphism

Polymorphism allows the same method name to have different implementations.

Example:

```python
class Bird:
    def sound(self):
        print("Bird Sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")
```

---

## 8. Encapsulation

Encapsulation protects data by restricting direct access.

Example:

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance
```

---

## 9. Abstraction

Abstraction hides implementation details and exposes only the necessary functionality.

It helps reduce complexity and improve code readability.

---

# 💻 Practice Programs

- Create a Student class
- Create an Employee class
- Create a Car class
- Practice constructors
- Create methods
- Practice inheritance
- Override methods using polymorphism
- Use private variables with encapsulation

---

# 🛠 Mini Project

## Student Management System

### Features

- Add Student Details
- Display Student Information
- Calculate Percentage
- Assign Grade
- Display Student Report

---

# 📂 Folder Structure

```
Day-11-OOP/
│
├── class_object.py
├── constructor.py
├── methods.py
├── inheritance.py
├── polymorphism.py
├── encapsulation.py
├── abstraction.py
├── student_management.py
└── README.md
```

---

# 🎯 Learning Outcome

By completing Day 11, I can:

- Understand the basics of Object-Oriented Programming.
- Create classes and objects.
- Use constructors (`__init__`).
- Define instance variables and methods.
- Apply inheritance to reuse code.
- Implement polymorphism by overriding methods.
- Protect data using encapsulation.
- Understand the concept of abstraction.
- Build simple object-oriented Python applications.

---

# 🧠 Key Takeaways

- OOP helps write clean and reusable code.
- A class is a blueprint, while an object is an instance of that class.
- Constructors initialize object data.
- Inheritance promotes code reuse.
- Polymorphism allows one interface with multiple implementations.
- Encapsulation improves data security.
- Abstraction hides unnecessary implementation details.

---

# 🚀 What's Next?

## Day 12 – Modules & Packages

Topics:
- Importing Modules
- Creating Custom Modules
- Built-in Modules
- Math Module
- Random Module
- Datetime Module
- Working with Packages

---

## 👨‍💻 Author

**Aryan Patil**

**21 Days Python Challenge 🐍**

> *"The best way to master Python is to practice consistently. Every day of coding is one step closer to becoming a better developer."*
