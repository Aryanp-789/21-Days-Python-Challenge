# 📅 Day 16 – File Handling in Python

## 📖 Overview

Welcome to **Day 16** of my **21-Day Python Challenge**!

Today, I learned how Python works with files. File handling allows programs to store, read, and update data permanently instead of keeping it only in memory.

---

## 🎯 Learning Objectives

* Understand file handling in Python
* Read data from text files
* Write data to files
* Append new data without deleting existing content
* Use the `with` statement for automatic file closing
* Handle file-related errors using exception handling

---

## 📚 Topics Covered

### 📂 File Handling

* What is file handling?
* Why file handling is important

### 📖 Reading Files

* `read()`
* `readline()`
* `readlines()`

### ✍️ Writing Files

* Creating new files
* Overwriting existing files

### ➕ Appending Data

* Adding new content using append mode (`a`)

### 🔐 Using `with`

* Automatic resource management
* Cleaner and safer code

### ⚠️ Exception Handling

* Handling `FileNotFoundError`
* Using `try` and `except`

---

## 🛠️ File Modes

| Mode | Description                                   |
| ---- | --------------------------------------------- |
| `r`  | Read a file                                   |
| `w`  | Write to a file (overwrites existing content) |
| `a`  | Append new content                            |
| `x`  | Create a new file                             |
| `rb` | Read a binary file                            |
| `wb` | Write a binary file                           |

---

## 💻 Practice Program

A simple Python program that:

* Creates a text file
* Writes student information
* Reads the stored data
* Appends additional information

---

## 📁 Project Structure

```
Day16-File-Handling/
│── file_handling.py
│── student.txt
└── README.md
```

---

## 🚀 What I Learned

* How to create and open files
* Different file modes and their uses
* Reading complete files and individual lines
* Writing and appending data
* Using `with open()` for better resource management
* Handling common file errors with exception handling

---

## 🎯 Mini Challenge

Create a program that:

1. Accepts the user's name.
2. Saves it in `names.txt`.
3. Reads and displays all saved names.

---

## 🧠 Key Takeaways

* File handling is essential for storing persistent data.
* Always close files after use or use the `with` statement.
* Exception handling prevents program crashes when files are missing.
* File handling is widely used in real-world applications such as logging, reports, databases, and configuration management.

---

## 📌 Outcome

By completing Day 16, I gained practical experience in reading, writing, and managing files in Python, along with writing safer and more reliable programs using exception handling.

---

### ⭐ Day 16 Completed Successfully!

**Next Topic:** Day 17 – Object-Oriented Programming (OOP): Classes and Objects
