# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Assignment 4: Hands On Python Data Structures


# Task 1 - Working with Lists

favoriteFruits = ["bananas", "Grapes", "Pineapple", "Mango", "Oranges"]
print("Original List: ",favoriteFruits)

favoriteFruits.append("Apple")
print("Item Added: ",favoriteFruits)

favoriteFruits.remove("Grapes")
print("Item Removed: ", favoriteFruits)

print(f"Reversed List: {favoriteFruits[::-1]}")
print("\n")

# Task 2 - Exploring Dictionaries

yourBoy = {"Name": "Jeffrey", "Age": 21, "City": "Chelsea"}
print(yourBoy)

yourBoy["Favorite Color"] = "Orange"
print(yourBoy)

yourBoy.update({"City": "Boston"})
print(yourBoy)

values = []
for pair in yourBoy: 
    values.append(str(yourBoy.get(pair)))

print("Keys: ", ", ".join(yourBoy.keys()))
print("Values: ", ", ".join(values))
print("\n")

#Task 3 - Using Tuples

favoriteTrifecta = ("Law Abiding Citizen", "Sleeptalk", "Hunger Games")
print("Trifecta of favorite things = ", favoriteTrifecta)

print("This line of code causes error because tuples are immutable: favoriteTrifecta[0] = 'Dawn of the Planets of the Apes'")
# favoriteTrifecta[0] = "Dawn of the Planets of the Apes"

print(f"Length of Tuple: {len(favoriteTrifecta)}")
