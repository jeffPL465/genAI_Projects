# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 3: Exploring String Methods


# Task 1: String Slicing and Indexing

#Assigning Variables
string1 = "Python is Amazing!"

#Extracting the word "Python"
print("The First Word is: " + string1[0:6] + "\n")

#Extracting the last word "Amazing"
print("The First Word is: " + string1[10:17] + "\n")

#Reverse the String
print("The Sentence Reversed is: " + string1[::-1] + "\n")


# Task 2: String Methods

#Assigning variables
string2 = " hello, python world! "

#Removing Extra Space
print("With the extra spaces stripped:" + string2.strip())

#Capitalizing the first letter
print("Capitalized First letter: " + string2.strip().capitalize())

#Replacing 'world' with 'universe'
print("Replaced 'world' with 'universe': " + string2.replace(string2[15:20], "universe").strip())

#Convert String to Uppercase
print("String Converted to Uppercase: " + string2.strip().upper())


#Task 3: Check for Palindromes

#Assigning variables
userInput = input("Enter a word Here: ")
string3 = userInput.lower()
reverseString3 = userInput[::-1].lower()

if string3 == reverseString3:
    print(f"Yes, {userInput} is a Palindrome")
else:
    print(f"No, {userInput} is not a Palindrome")