# Create a program that ask the user to input a complete statement. Print the number of words in the input.

# Ask the user to input a complete statement
statement = input("Enter a statement: ")

# Split the statement into words and count the number of words
word_count = len(statement.split())

# Display the number of words in the statement
print("Number of words in the statement:", word_count)