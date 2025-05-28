# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Password Strength Checker


# Assigning Variables (password == input, violations == list, passwordStrength == string, everything else == int)
password = input("Enter Password Here: ")
passMinimum = 8
numLower = 0
numUpper = 0
numDigit = 0
numSpecial = 0
passwordRating = 5
passwordStrength = ""
violations = []


# Create means of identifying different characters in password
#for every character in password, check if the char is a lowercase, uppercase, special or digit
for i in range(0,len(password)):
    if password[i].islower():   #if character in password is lowercase, add 1 to numLower
        numLower += 1

    if password[i].isupper():   #if character in password is uppercase, add 1 to numUpper
        numUpper += 1

    if password[i].isdigit():   #if character in password is a digit, add 1 to numDigit
        numDigit += 1
    
    if password[i].isdigit() == False and password[i].isupper() == False and password[i].islower() == False:
        numSpecial += 1     #if character in password is not either of the other 3, then it is a special character
    

# Applying a message for each type of violation
#Append the type of error to the list of violations based on whether the 'num...' variables show that one of the requirements haven't been met
if numLower < 1:
    violations.append("one lowercase number")

if numUpper < 1:
    violations.append("one uppercase number")

if numDigit < 1:
    violations.append("one digit")

if numSpecial < 1:
    violations.append("one special character")


# Password Rating and Strength Section  

numStrength = len(password)

#If there are no violations then determine the strength of the password
if len(violations) == 0: 
    if numStrength > 8:  
        passwordRating = passwordRating + (numStrength - 8)     #Password gets higher rating with more characters than the base of 8
    elif numStrength == 8 and numSpecial == 2 and numLower == 2 and numUpper == 2 and numDigit == 2:
        passwordRating = 7      #Special case in which 8 character password gives a decent rating 
    else:
        passwordRating = 5      #Base Rating for 8 char password that isn't special case

#Giving Messages based on the rating of the password (5-6 = weak / 7-8 = solid / 9-10 = strong)
if passwordRating >= 7 and passwordRating < 9:
    passwordStrength = "Solid"
elif passwordRating >= 9:
    passwordStrength = "Strong"
else:
    passwordStrength = "Weak"

if passwordRating >= 10:    #If the pasword rating exceeds 10/10, then rating stays at 10
    passwordRating = 10


# Putting everything together
if len(password) >= passMinimum: 
    if numLower < 1 or numUpper < 1 or numDigit < 1 or numSpecial < 1:
            print('Your password needs at least', ' and '''.join(violations))
    else:
        print("Your password is sufficient!", "\n")
        print(f"The password you used is {passwordStrength}. \nRating: {passwordRating}/10")     
else: 
    print("Insufficient amount of characters")


