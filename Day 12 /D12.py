import os

filename = "notes.txt"

# Write to a file
with open(filename, "w") as file:
    file.write("Welcome to Day 12 of Python Challenge!\n")
    file.write("Learning File Handling in Python.\n")

print("Data written successfully!")

# Read the file
with open(filename, "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Append data
with open(filename, "a") as file:
    file.write("This line is added using append mode.\n")

print("\nData appended successfully!")

# Read again
with open(filename, "r") as file:
    print(file.read())

# Check if file exists
if os.path.exists(filename):
    print("\nThe file exists.")
else:
    print("\nThe file does not exist.")
