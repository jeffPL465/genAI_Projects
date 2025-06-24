# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 6: Check Your Knowledge About Errors


#Task 1
# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except ValueError:
#     print("That is not a valid input, please try again")
# except ZeroDivisionError:
# print("You can't divide by zero, please try again.")


#Task 2
animal_list = ["Panda", "Gorilla", "Grizzly Bear"]
animal_weight = {"Panda": 280, "Gorilla": 350, "Grizzly": 680}

try:
    animal_list[5]
except IndexError:
    print("IndexError has occured! List index out of range.")


try:
    animal_weight["Lion"]
except KeyError:
    print("KeyError has occured! Key was not found in the dictionary.")

try:
    animal_Combination = animal_list[0] + animal_weight.get("Panda")
except TypeError:
    print("TypeError has occured! Unsupported operand types.")
else:
    print(animal_Combination)


#Test 3
try:
    dividend = int(input("Enter Dividend Here: "))
    divisor = int(input("Enter Divisor Here: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Input value must be a number.")
else: 
    print(f"The division between the two numbers is: {result}")
finally:
    print("Thank you, we hope to help you with division again!")