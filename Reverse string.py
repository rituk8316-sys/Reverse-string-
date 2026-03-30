# Program to Reverse a String
# Author: Your Name
# Description: This program takes a string input and prints its reverse

def reverse_string(text):
    reversed_text = ""
    
    # Loop to reverse string
    for char in text:
        reversed_text = char + reversed_text
    
    return reversed_text


# Taking input from user
input_string = input("Enter a string: ")

# Calling function
result = reverse_string(input_string)

# Displaying output
print("Reversed string is:", result)
