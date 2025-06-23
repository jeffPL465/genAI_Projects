# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: About Menu


# Factorial Function
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

# Fibonacci Function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


user_choice = input("Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Draw a Recursive Fractal 4. Exit ")

if int(user_choice) == 1:
    print("\n")
    factorial_num = input("Enter a Number to Find its Factorial ")
    print("\n")
    print(f"The Factorial of {int(factorial_num)} is {factorial(int(factorial_num))}")

elif int(user_choice) == 2:
    print("\n")
    fibonacci_num = input("Enter a Number to Find the Fibonacci Equivelant ")
    print("\n")
    print(f"The Fibonacci Equivalent of {int(fibonacci_num)} is {fibonacci(int(fibonacci_num))}")

elif int(user_choice) == 3:
    print("\n")
    print("Sorry, feature yet to be implemented :(")

elif int(user_choice) == 4:
    print("\n")
    print("You are now Exiting. Thanks for the visit, hopefully we will cross paths again :)")

else:
    print("\n")
    print("Sorry, the number you input is invalid, please try again.")