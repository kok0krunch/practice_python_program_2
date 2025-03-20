# Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# Ask user to input their fullname
fullname = input("Enter your fullname: ")

# Format fullname in a lower case and split it by words.
lower_fullname = fullname.lower().split()