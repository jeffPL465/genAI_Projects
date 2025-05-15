# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Eligible Elector

#Assigning variables (age = user inputs their age) (eligibleAge = 18 to specify what an eligible age is)
age = int(input("Hello, to check your eligibility please input your age here: "))
eligibleAge = 18

#Conditional Statement

if age >= eligibleAge: #If the users age is greater than or equal to 18
    print("Congratulations! You're eligible to vote - Your voice can make a difference.")                               #They're good
elif age >= 15 and age < eligibleAge: #To distinguish a user who is close to the eligible age (15 - 17)
    print("Unfortunately, you're not eligible yet. But you're so close! Only", eligibleAge - age, "more years!")        #They're not good
else: #This user is not old enough to start counting the years left (encourage them to wait a while longer)
    print("Sadly, you're not eligible yet. There's still a bit left to go until you are but it'll be worth the wait!")  #They're very not good