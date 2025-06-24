# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Calculator with Exception Handling 


def not_an_option(num):
    if num < 1 or num > 5:
        raise ValueError("Input value must be a number between 1 and 5, please try again.")
    

user_choice = int(input("\nWelcome to Calc help online! Please explore our options below! \nChoose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit \nPlease Choose Here: "))


if user_choice == 1:
    try:
        num1 = int(input("Enter first number here: "))
        num2 = int(input("Enter second number here: "))
        result = num1 + num2
    except ValueError:
        print("Input has to be a number, Please try again.")
    else: 
        print(f"The Sum of {num1} and {num2} is {result}")
    finally:
        print("\nThank you for using our online calculator! We hope to see you again soon.")

elif user_choice == 2:
    try:
        num1 = int(input("Enter first number here: "))
        num2 = int(input("Enter second number here: "))
        result = num1 - num2
    except ValueError:
        print("Input has to be a number, Please try again.")
    else:
        print(f"The difference between {num1} and {num2} is {result}")
    finally:
        print("\nThank you for using our online calculator! We hope to see you again soon.")


elif user_choice == 3:
    try:
        num1 = int(input("Enter first number here: "))
        num2 = int(input("Enter second number here: "))
        result = num1 * num2
    except ValueError:
        print("Input has to be a number, Please try again.")
    else:
        print(f"The Product of {num1} and {num2} is {result}")
    finally:
        print("\nThank you for using our online calculator! We hope to see you again soon.")

elif user_choice == 4:
    try:
        num1 = int(input("Enter first number here: "))
        num2 = int(input("Enter second number here: "))
        result = num1 / num2
    except ValueError:
        print("Input has to be a number, Please try again.")
    except ZeroDivisionError:
        print("Oops, you tried to divide by 0. Please try again.")
    else:
        print(f"The Quotient between {num1} and {num2} is {result}")
    finally:
        print("\nThank you for using our online calculator! We hope to see you again soon.")

elif user_choice == 5:
    print("Thank you for using our online calculator! We hope to see you again soon.")

else:
    try:
        not_an_option(user_choice)
    except ValueError as e:
        print(e)