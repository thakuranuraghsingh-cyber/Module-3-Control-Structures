# Task 2: Write and Append Data to a File

filename = "output.txt"

# Take input and write to the file
write_to_file = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(write_to_file + "\n")
print(f"Data successfully written to {filename}.\n")

# Appends additional data to the same file.
append_file = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(append_file + "\n")
print("Data successfully appended.\n")

# Read and display final content of the file
print(f"Final content of {filename}:")
with open(filename, "r") as file:
    print(file.read())
