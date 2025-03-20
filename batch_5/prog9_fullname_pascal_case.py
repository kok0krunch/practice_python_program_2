# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# Ask user to input their fullname
fullname = input("Enter your fullname: ")

# Format fullname in a proper case and split it by words.
proper_fullname = fullname.title().split()

# Remove spaces by joining the words together.
pascal_fullname = "".join(proper_fullname)