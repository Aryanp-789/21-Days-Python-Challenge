# 🐍 Day 17 – File Handling in Python

## 📌 21-Day Python Challenge

Welcome to **Day 17** of my 21-Day Python Challenge!

Today, I learned about **File Handling in Python**. File handling allows us to create, read, write, and update files using Python programs.

---

## 📚 Topics Covered

* Introduction to File Handling
* Opening a File
* Closing a File
* File Modes
* Reading Data from a File
* Writing Data to a File
* Appending Data to a File
* Using the `with open()` Statement
* Basic Exception Handling with Files
* Mini Project – Student Record Manager

---

## 📂 What is File Handling?

File handling is used to store data permanently in a file.

Normally, variables store data temporarily while a program is running. Once the program stops, the data is lost.

Files allow us to save data permanently.

Example:

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

---

## 🔓 Opening a File

Python provides the `open()` function to open a file.

### Syntax

```python
file = open("filename.txt", "mode")
```

Example:

```python
file = open("data.txt", "r")
```

---

## 📋 File Modes in Python

| Mode | Description                                         |
| ---- | --------------------------------------------------- |
| `r`  | Read an existing file                               |
| `w`  | Write data to a file and overwrite existing content |
| `a`  | Append new data without deleting existing content   |
| `x`  | Create a new file                                   |
| `b`  | Open a file in binary mode                          |
| `t`  | Open a file in text mode                            |

---

## 📖 Reading a File

### Using `read()`

The `read()` method reads the complete content of a file.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 📄 Using `readline()`

The `readline()` method reads one line at a time.

```python
with open("example.txt", "r") as file:
    line = file.readline()
    print(line)
```

---

## 📑 Using `readlines()`

The `readlines()` method returns all lines as a list.

```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

---

## ✍️ Writing to a File

The `w` mode is used to write data to a file.

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
```

⚠️ **Important:** The `w` mode deletes the existing content before writing new content.

---

## ➕ Appending Data to a File

The `a` mode adds new data without deleting existing content.

```python
with open("example.txt", "a") as file:
    file.write("\nWelcome to Day 17!")
```

---

## 🔒 Using `with open()`

The recommended way to work with files is using the `with` statement.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Advantages

* Automatically closes the file
* Makes the code cleaner
* Reduces the chance of errors

---

## ⚠️ Exception Handling with Files

We can use `try-except` to handle file-related errors.

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")
```

---

# 🚀 Mini Project – Student Record Manager

In this mini project, I created a simple Student Record Manager using Python File Handling.

## Features

* Add student records
* Save student data to a file
* View all student records
* Keep previous records using append mode
* Handle missing files using exception handling

---

## 💻 Python Code

```python
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name}, {roll_no}, {marks}\n")

    print("Student record added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.read()

            if records:
                print("\n--- Student Records ---")
                print(records)
            else:
                print("No student records found.")

    except FileNotFoundError:
        print("Student record file does not exist.")


while True:

    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")
```

---

## 📁 Project Structure

```text
Day-17-File-Handling/
│
├── README.md
├── file_handling.py
├── student_record_manager.py
└── students.txt
```

---

## 🧠 What I Learned

Today, I learned:

* How to open and close files in Python
* How different file modes work
* How to read data from files
* How to write data to files
* How to append new content
* How to use the `with open()` statement
* How to handle `FileNotFoundError`
* How to build a simple project using file handling

---

## 🎯 Day 17 Completed

Successfully completed **Day 17 of my 21-Day Python Challenge**.

Today’s focus was understanding **File Handling in Python** and implementing the concepts by building a **Student Record Manager**.

Only **4 more days to go!** 🚀🐍

#Python #PythonProgramming #21DaysPythonChallenge #FileHandling #CodingChallenge #LearnPython #GitHub #Programming

