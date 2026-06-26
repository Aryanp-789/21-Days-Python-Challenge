# Day 10 - File Handling

# Write to a file
with open("notes.txt", "w") as file:
    file.write("Welcome to Day 10 of Python Challenge!\n")
    file.write("Today I learned File Handling.\n")

print("Data written successfully.")

# Read the file
with open("notes.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Append new data
with open("notes.txt", "a") as file:
    file.write("This line was added using append mode.\n")

print("\nNew data appended successfully.")

# Read updated file
with open("notes.txt", "r") as file:
    print("\nUpdated File:")
    print(file.read())
