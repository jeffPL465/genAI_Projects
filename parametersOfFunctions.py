# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 5: About Parameters of Functions


#Task 1
def greet_user(name):
    print(f"Hello, {name}! We're Excited to Have You!")
    return " "

def add_numbers(a, b):
    return a + b

print(f"{greet_user("Jeffrey")} \nThe sum of 7 and 8 is {add_numbers(7, 8)}")


#Task 2

def describe_pet(pet_name, animal_type = "dog"):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("LongTanandHandsome", "Giraffe")


#Task 3
def make_sandwich(*args):
    sandwich_ingredients = []
    for ingredient in args:
        sandwich_ingredients.append(ingredient)

    print(f"Our sandwich will have the following ingredients: ", " - ".join(sandwich_ingredients))

make_sandwich("ham", "cheese", "lettuce", "tomato", "mayo")


#Task 4
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

print(factorial(6))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    
print(fibonacci(6))