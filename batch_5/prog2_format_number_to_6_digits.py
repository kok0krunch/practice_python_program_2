# Create a program that ask the user to input a number (0-1000). 
# Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# Ask user to input a number
number = input("Enter a number (0-1000): ")

# Format the nuber to 6 digit with leading zeros
formatted_number = number.zfill(6)