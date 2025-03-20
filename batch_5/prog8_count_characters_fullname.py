# Create a program that ask the user to input their fullname. Print the number of characters in the input.

# Ask user to input their fullname
fullname = input("Enter your fullname: ")

# Count the number of characters in the fullname
num_characters = len(fullname.replace(" ", ""))

# Print the number of characters in the fullname
print("Number of characters in your fullname:", num_characters)