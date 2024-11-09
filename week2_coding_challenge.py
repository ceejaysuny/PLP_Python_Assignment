"""
Tasks:

Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. 
Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, 
such as their name, age, and favorite color.
 Ask the user for input and store the information in the dictionary. 
 Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers.
 Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. 
Then, use list comprehension to create a new list that 
contains only the words that have an odd number of characters.

These tasks should test your understanding of basic concepts related to lists, tuples, dictionaries, and sets in Python. Good luck!
"""

### 1. Program to create a list of integers and compute their sum

# Task 1
# Accepts user input to create a list of integers
int_list = input("Enter a list of integers separated by spaces: ").split()
int_list = [int(x) for x in int_list]

# Compute the sum of all integers in the list
sum_of_integers = sum(int_list)
print("The sum of all integers is:", sum_of_integers)


### 2. Create a tuple of favorite books and print each book name

# Task 2
# Create a tuple containing the names of five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Moby Dick")

# Print each book name on a separate line using a for loop
for book in favorite_books:
    print(book)


### 3. Program to store personal information in a dictionary

# Task 3
# Create a dictionary to store information about a person
person_info = {}

# Ask the user for input and store the information in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("Person Information:", person_info)


### 4. Program to find common elements between two sets

# Task 4
# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

# Create a new set that contains only the elements common to both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


### 5. Program to filter words with an odd number of characters

# Task 5
# Store a list of words
words = ["hello", "world", "python", "code", "programming"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with an odd number of characters:", odd_length_words)

