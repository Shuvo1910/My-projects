# Resturent manu and order:
manu = {
    'Coffee':40,    
    'Burger':60,
    'Sandwitch':80,
    'Pizza':150,
    'Drinks':30,
    'Water':15
}
print("Welcome to MY Resturant")

# \n print One under the other.
print("Coffee   : TK40\nBurger   : TK60\nSandwitch : TK80\nPizza    : TK150\nDrinks   : TK30\nWater    : TK15")
order_total = 0

# take input from the user.
item_1 = input("Your wanted item = ")
if item_1 in manu:
    order_total += manu[item_1] 
    print(f"Your {item_1} has been added")
else:
    print(f"Sorry, This {item_1} is not available")
another_order = input("Do you want another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter your second item = ")
    if item_2 in manu:
        order_total += manu[item_2]
        print(f"Item {item_2} has been added")
    else:
        print(f"Sorry, This {item_2} is not available")
print(f"Your payment is", order_total )


































