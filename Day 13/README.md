# 🐍 Day 13 – File Handling in Python

Welcome to **Day 13** of my **21-Day Python Challenge**! 🚀

Today I learned one of the most useful concepts in Python—**File Handling**. File handling allows programs to store data permanently instead of keeping it only in memory. It is widely used in real-world applications such as note-taking apps, student management systems, banking software, inventory systems, and logging systems.

---

# 📚 Topics Covered

* Introduction to File Handling
* Opening Files
* File Modes (`r`, `w`, `a`, `x`)
* Reading Files
* Writing to Files
* Appending Data
* Reading Line by Line
* Using the `with` Statement
* Checking File Existence
* Handling File Exceptions
* Mini Project – Student Notes Manager

---

# 📖 What is File Handling?

File handling is the process of creating, reading, writing, updating, and deleting files using Python. It enables applications to save information permanently.

Example uses include:

* Saving user information
* Storing application settings
* Keeping logs
* Managing reports
* Saving notes
* Reading configuration files

---

# 📂 File Modes

| Mode | Description                                                        |
| ---- | ------------------------------------------------------------------ |
| `r`  | Read an existing file                                              |
| `w`  | Write to a file (creates a new file or overwrites an existing one) |
| `a`  | Append data to the end of a file                                   |
| `x`  | Create a new file (fails if the file already exists)               |
| `rb` | Read a binary file                                                 |
| `wb` | Write a binary file                                                |

---

# 💻 Programs Implemented

### 1. Create and Write to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello Python!")
```

---

### 2. Read a File

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

### 3. Append Data

```python
with open("notes.txt", "a") as file:
    file.write("\nLearning File Handling")
```

---

### 4. Read Line by Line

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### 5. Check if File Exists

```python
import os

if os.path.exists("notes.txt"):
    print("File exists")
else:
    print("File not found")
```

---

### 6. Handle Missing File

```python
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

# 🚀 Mini Project – Student Notes Manager

## Features

* Add Notes
* Save Notes Permanently
* View Saved Notes
* Handle Missing Files Gracefully
* Simple Menu-Based Interface

This project demonstrates how file handling can be used to build practical applications.

---

# 📁 Project Structure

```
Day13/
│
├── file_handling.py
├── student_notes.py
├── notes.txt
└── README.md
```

---

# 🧠 Key Learnings

* Learned how to create text files using Python.
* Understood different file modes and their purposes.
* Read complete files and individual lines.
* Appended new data without deleting existing content.
* Used the `with` statement for automatic file closing.
* Checked file existence before accessing it.
* Handled file-related exceptions using `try` and `except`.
* Built a simple project that stores data permanently.

---

# 🌍 Real-World Applications

* Student Management Systems
* Banking Applications
* Employee Record Systems
* Note-Taking Applications
* Inventory Management
* Expense Tracker
* Log File Generation
* Configuration Files
* Report Generation
* Data Storage

---

# 📈 Skills Improved

* Python Basics
* File Handling
* Problem Solving
* Exception Handling
* Data Persistence
* Program Organization

---

# 📝 Practice Questions

* Create a file and write your name into it.
* Read data from a text file.
* Append your city name to an existing file.
* Display the file content line by line.
* Check whether a file exists before opening it.
* Create a simple Notes Manager using file handling.
* Count the number of lines in a file.
* Count the number of words in a file.
* Copy the contents of one file into another.
* Read only the first five lines of a file.

---

# 🎯 Outcome

By completing Day 13, I gained practical experience with Python file handling. I can now create, read, update, and manage files while writing cleaner and safer code using the `with` statement and exception handling. These skills are essential for developing real-world Python applications.

---

# 📌 Challenge Progress

* ✅ Day 13 Completed
* 🔥 13/21 Days Finished
* ⏳ 8 Days Remaining

---

## ⭐ If you found this repository helpful, consider giving it a star!

### Connect with Me

* **GitHub:** https://github.com/Aryanp-789
* **LinkedIn:** [www.linkedin.com/in/aryan-patil-71319a256](http://www.linkedin.com/in/aryan-patil-71319a256)

**#Python #PythonChallenge #100DaysOfCode #FileHandling #LearningInPublic #Programming #Coding #DeveloperJourney**
