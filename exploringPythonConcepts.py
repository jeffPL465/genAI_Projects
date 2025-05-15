# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 1: Exploring Python Concepts


# Task 1 - Variables: Your first Python Intro

#Assigning Variables (name, age, height, major, school and ethnicity)
name = "Jeffrey Ponce"
age = 21
height = 5.6
major = "Electrical and Computer Engineering"
school = "Worcester Polytechnic Institute"
ethnicity = "Honduran"

#printing message with all variables
print("Hello, My name is", name, "and I am a", age, "year old", major, "student at", school, ". I am", height, "and come from a", ethnicity, "background")
print("\n")

# Task 2 - Operators: Playing with numbers

#Assigning variables
num1 = 10
num2 = 5

#Addition
print("If there are 5 people in the rooms and 10 in the hallway, there are", num1 + num2, "people in the house in total")
print("\n")

#Subtraction
print("I had 10 dollars but I lost 5 in a bet, now I only have", num1 - num2, "dollars left")

#Multiplication
print("There are 5 boxes, each filled with 10 pencils, there are", num1 * num2, "pencils in total")
print("\n")

#Division
print("There were 10 necklaces laid out on the desk, but the store clerk said I could only try on a fifth of them. So I tried on", int(num1 / num2), "necklaces in total")
print("\n")


# Task 3 - Conditional Statements: The Number Checker

#User input of number to be checked
number = input("Enter a Number: ")

#Positive, Negative and Zero Checker

if int(number) > 0:
    print("The number " + number + " is positive!")
elif int(number) < 0:
    print("The number " + number + " is negative :( ")
else: 
    print("The number is zero")