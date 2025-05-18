# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 2: Explore Loops in Python


# Task 1 - Counting Down With Loops

# Assigning x as an input number that is converted into an int
x = int(input("Enter a Number To Start the Countdown "))

# Main Loop
while x > 0:                        # While x is greater than zero
    print(f"Game Starts in {x}")    # Display current x value
    x -= 1                          # decrement the x value by 1
    if x <= 0:                      # if statement saying that if x gets down to zero
        print("GAME START")         # Then a message is displayed "GAME START"

# If the input number is below zero then tell the user the number is invalid
if x < 0:
    print("Invalid Start Time, Try Again :(")

print("\n")


# Task 2 - Multiplication Table with for Loops

# Assigning y as an input number that is converted into an int
y = int(input("Enter a Number for the Times Table "))

# Print initial message and then go into main loop
print(f"The times table for {y} is: \n")
for i in range(1, 11):                                 #set the range for the times table
    print(f"{y} * {i} = {y * i}", end = "\n")

print("\n")


# Task 3 - Find the Factorial

# Assigning variables
factorial = 0
z = int(input("Input the Number for the Factorial:"))


for i in range(z + 1):
    if i == 0 or factorial == 0:
        factorial += 1
    else:
        factorial *= i

print(f"The factorial of {z} is {factorial}")