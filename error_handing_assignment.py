# Task 1 : Python program to read a file and handle errors
filename = "sample.txt"

# Create the file with given content
with open(filename, "w") as file:
    file.write("Line 1: This is a sample text file.\n")
    file.write("Line 2: It contains multiple lines.\n")
try:
    # Try Opens and reads a text file
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        # Read and Prints its content
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # Handles errors gracefully if the file does not exist
    print("Error: The file 'sample.txt' was not found.")