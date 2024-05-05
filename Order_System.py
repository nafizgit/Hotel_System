#define the menu of Restaurant
menu = {
    "Faluda": 100,
    "Pasta": 50,
    "Coffee": 90,
    "black Tea": 20,
    "Cold Coffee": 80,

}
#Greet
print("Welcome To CodeVibe Restaurant!")
print("Faluda: 100Tk\nPasta: 50Tk\n Coffee: 90Tk\n black Tea: 20Tk\n Cold Coffee: 80TK")

order_total = 0
item_1 = input("Enter What You wanna Order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} not available yet! sorry")

another_order = input("Do you want to add another item?(Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter Second Item = ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
else:
    print(f"order item {item_2}is not available!")
print(f"The total amount of items to pay is {order_total}")