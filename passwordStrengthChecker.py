# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Password Strength Checker


#Assigning Variables
password = input("Enter Password Here: ")
passMinimum = 8
numLower = 0
numUpper = 0
numDigit = 0
numSpecial = 0
passwordRating = 5
passwordStrength = ""
violations = []

for i in range(0,len(password)):
    if password[i].islower():
        numLower += 1

    if password[i].isupper():
        numUpper += 1

    if password[i].isdigit():
        numDigit += 1
    
    if password[i].isdigit() == False and password[i].isupper() == False and password[i].islower() == False:
        numSpecial += 1
    

if numLower < 1:
    violations.append("one lowercase number")

if numUpper < 1:
    violations.append("one uppercase number")

if numDigit < 1:
    violations.append("one digit")

if numSpecial < 1:
    violations.append("one special character")

#Password Rating Section  

numStrength = len(password)

if len(violations) == 0: 
    if numStrength > 8: 
        passwordRating = passwordRating + (numStrength - 8)
    elif numStrength == 8 and numSpecial == 2 and numLower == 2 and numUpper == 2 and numDigit == 2:
        passwordRating = 7
    else:
        passwordRating = 5

if passwordRating >= 7 and passwordRating < 9:
    passwordStrength = "Solid"
elif passwordRating >= 9:
    passwordStrength = "Strong"
else:
    passwordStrength = "Weak"

if passwordRating >= 10:
    passwordRating = 10

if len(password) >= passMinimum: 
    if numLower < 1 or numUpper < 1 or numDigit < 1 or numSpecial < 1:
            print('Your password needs at least', ' and '''.join(violations))
    else:
        print("Password is sufficient!", "\n")
        print(f"Your Password is {passwordStrength} \n Rating: {passwordRating}/10")     
else: 
    print("Insufficient amount of characters")


