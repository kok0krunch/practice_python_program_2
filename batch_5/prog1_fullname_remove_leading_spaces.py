# Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# Ask user to input their fullname with leading spaces
name = input("Enter your full name with leading spaces: ")

# Remove leading spaces using lstrip() method
fullname = name.lstrip()