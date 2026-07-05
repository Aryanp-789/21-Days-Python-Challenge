file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()

with open("sample.txt", "r") as file:
    print(file.read())
