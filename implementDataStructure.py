# Jeffrey Ponce Lopez
# Cognizant GenAI Externship
# Project: Implement Your Own Data Structure

#Steps 1 and 2
print("\n")
inventory = {"Apple": (20, 1.25), "Banana": (60, 0.64), "Chicken": (30, 10.25), "Beef": (25, 12.5)}
print(f"Original Inventory: {inventory}")
inventory["Doritos"] = (40, 4.5)
print(f"Inventory With Item Added: {inventory}")
del inventory["Apple"]
print(f"Inventory With Item Removed: {inventory}")
inventory.update({"Banana": (50, 0.7)})
print(f"Updated Inventory: {inventory}")
print("\n")

#Step 3
inventoryItem = iter(inventory)

print("Welcome to our Online Inventory! Here you can see the items we have on stock, its quantity and price. \n")
print("For our Premium Members, there is also the option to purchase and reserve the entirety of any item in our inventory \n" \
      "with the total cost shown below. \n")
print("We hope you find everything you need and thank you for shopping at Ponce Online Inventory. \n")
for item in inventory: 
    print(f"Item: {next(inventoryItem)}, \n Quantity: ${inventory.get(item)[0]}, \n Price: ${inventory.get(item)[1]},")
    print(f" Total Price: ${inventory.get(item)[1] * inventory.get(item)[0]} \n")

