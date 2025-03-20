# Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# Ask user to input their fullname
fullname = input("Enter your fullname: ")

# Format fullname in a lower case and split it by words.
lower_fullname = fullname.lower().split()

# Join the words in fullname with underscore.
snake_case = "_".join(lower_fullname)

# Print the fullname in snake case.
print("Fullname in snake case is:", snake_case)