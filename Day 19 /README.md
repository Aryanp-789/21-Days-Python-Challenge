# 🐍 Day 19 – Working with JSON in Python

Welcome to **Day 19 of my 21-Day Python Challenge!** 🚀

Today, I learned about **JSON (JavaScript Object Notation)** and how to work with JSON data in Python.

JSON is one of the most commonly used data formats for storing and exchanging data between applications, APIs, servers, and databases.

---

## 📚 Topics Covered

* What is JSON?
* JSON syntax and structure
* Python `json` module
* Converting Python objects to JSON
* Converting JSON data to Python objects
* Reading data from JSON files
* Writing data to JSON files
* Using `json.dumps()`
* Using `json.loads()`
* Using `json.dump()`
* Using `json.load()`
* Pretty printing JSON data

---

## 🔹 What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight data format used to store and exchange data.

Example:

```json
{
    "name": "Aryan",
    "age": 22,
    "skills": ["Python", "JavaScript", "React"]
}
```

JSON data is commonly used in:

* Web APIs
* Web applications
* Mobile applications
* Configuration files
* Data exchange between frontend and backend

---

## 🔹 Importing the JSON Module

Python provides a built-in `json` module.

```python
import json
```

No additional installation is required.

---

## 🔹 Converting Python Data to JSON

The `json.dumps()` method converts a Python object into a JSON string.

```python
import json

student = {
    "name": "Aryan",
    "age": 22,
    "course": "Computer Science"
}

json_data = json.dumps(student)

print(json_data)
```

### Output

```text
{"name": "Aryan", "age": 22, "course": "Computer Science"}
```

---

## 🔹 Pretty Printing JSON

We can use the `indent` parameter to make JSON data more readable.

```python
import json

student = {
    "name": "Aryan",
    "age": 22,
    "skills": ["Python", "React", "Node.js"]
}

json_data = json.dumps(student, indent=4)

print(json_data)
```

### Output

```json
{
    "name": "Aryan",
    "age": 22,
    "skills": [
        "Python",
        "React",
        "Node.js"
    ]
}
```

---

## 🔹 Converting JSON to Python

The `json.loads()` method converts a JSON string into a Python object.

```python
import json

json_data = '{"name": "Aryan", "age": 22, "city": "Pune"}'

student = json.loads(json_data)

print(student)
print(student["name"])
print(student["city"])
```

### Output

```text
{'name': 'Aryan', 'age': 22, 'city': 'Pune'}

Aryan

Pune
```

---

## 🔹 Writing Data to a JSON File

The `json.dump()` method is used to write Python data into a JSON file.

```python
import json

student = {
    "name": "Aryan",
    "age": 22,
    "course": "Computer Science",
    "skills": ["Python", "JavaScript", "React"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data successfully written to student.json")
```

---

## 🔹 Reading Data from a JSON File

The `json.load()` method is used to read JSON data from a file.

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(student["name"])
print(student["skills"])
```

---

## 🔹 Difference Between JSON Methods

| Method         | Purpose                               |
| -------------- | ------------------------------------- |
| `json.dumps()` | Converts Python object to JSON string |
| `json.loads()` | Converts JSON string to Python object |
| `json.dump()`  | Writes Python data to JSON file       |
| `json.load()`  | Reads JSON data from JSON file        |

---

## 💻 Mini Project – Student Data Management System

In today's mini project, I created a simple Student Data Management System using Python and JSON.

### Features

* Add student information
* Store student data in JSON format
* Read student data from JSON file
* Display all students

### Python Code

```python
import json


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully!")


def display_students():

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        print("\nStudent Records")

        for student in students:
            print("--------------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

    except FileNotFoundError:
        print("No student records found.")


while True:

    print("\nStudent Data Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
```

---

## 📂 Project Structure

```text
Day-19-JSON/
│
├── README.md
├── json_basics.py
├── write_json.py
├── read_json.py
├── student_management.py
└── students.json
```

---

## 🎯 What I Learned

Today, I learned:

* How JSON works
* How to use Python's built-in `json` module
* How to convert Python objects into JSON
* How to convert JSON into Python objects
* How to read data from JSON files
* How to write data into JSON files
* How JSON is used for storing structured data
* How to build a simple project using Python and JSON

---

## 🌍 Real-World Uses of JSON

JSON is widely used in modern software development.

Some common examples include:

* REST APIs
* Frontend and backend communication
* Configuration files
* Web applications
* Mobile applications
* Data storage
* Third-party API responses

As I am learning **Python Full Stack Development**, understanding JSON is important because JSON is commonly used to exchange data between the frontend and backend.

---

## 🚀 Challenge Progress

**Day 19 of 21 Completed ✅**

```text
██████████████████░░ 90%
```

Only **2 more days to go!** 🔥

I am getting closer to completing my **21-Day Python Challenge**.

---

## 🔜 What's Next?

### Day 20 – APIs and HTTP Requests in Python

In the next challenge, I will learn:

* What is an API?
* What are HTTP requests?
* GET requests
* Working with the `requests` library
* Fetching data from a public API
* Handling JSON API responses
* Building a small API-based Python project

---

⭐ If you found this repository useful, feel free to star it!

#Python #JSON #PythonProgramming #21DaysOfPython #CodingChallenge #LearningInPublic #GitHub
