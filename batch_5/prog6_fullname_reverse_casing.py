# Create a program that ask the user to input their fullname in incorrect casing. 
# Print each character of the input in reverse casing.

# Ask user to input their fullname
fullname = input("Enter your fullname: ")

# Print each character of the fullname in reverse casing
print("Your fullname in reverse casing is:", fullname.swapcase())