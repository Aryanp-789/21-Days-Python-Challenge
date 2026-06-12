# Day 6 - Python Loops

## Introduction

Today I learned about loops in Python. Loops allow us to execute a block of code multiple times, making programs shorter and more efficient.

## Topics Covered

### For Loop

A for loop is used when the number of iterations is known.

```python
for i in range(1, 6):
    print(i)
```

### While Loop

A while loop runs until a condition becomes false.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Break Statement

The break statement stops the loop immediately.

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

### Continue Statement

The continue statement skips the current iteration and moves to the next iteration.

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

## Practice Program

```python
print("=== FOR LOOP ===")
for i in range(1, 6):
    print("Number:", i)

print("\n=== WHILE LOOP ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n=== BREAK EXAMPLE ===")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("\n=== CONTINUE EXAMPLE ===")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

## Output

```
=== FOR LOOP ===
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

=== WHILE LOOP ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

## Key Learnings

- Loops help automate repetitive tasks.
- The for loop is used when the number of repetitions is known.
- The while loop is used when repetition depends on a condition.
- break exits the loop immediately.
- continue skips the current iteration.

## Real-World Applications

- Data processing
- Automation scripts
- Game development
- File handling
- Data analysis

## Challenge Status

✅ Day 6 Completed

### Author
Aryan Patil

### Challenge
21 Days Python Challenge 🚀
