print("===========*Shopping center*============")
print("Availabel items in our shop!")
items = {
    101: ("Rice", 60),
    102: ("Wheat Flour", 45),
    103: ("Sugar", 50),
    104: ("Salt", 20),
    105: ("Cooking Oil", 140),
    106: ("Milk", 60),
    107: ("Bread", 35),
    108: ("Biscuits", 20),
    109: ("Tea Powder", 120),
    110: ("Coffee", 180),
    111: ("Soap", 30),
    112: ("Shampoo", 90),
    113: ("Toothpaste", 60),
    114: ("Toothbrush", 25),
    115: ("Detergent", 110),
    116: ("Pen", 10),
    117: ("Pencil", 5),
    118: ("Notebook", 40),
    119: ("Water Bottle", 100),
    120: ("Chocolate", 20)
}
for item_id, details in items.items():
    print(item_id, "-", details[0], "- ₹", details[1])

get_id=int(input("enter id of item:"))
quantity=int(input("enter quantity of items"))
print("-------BILL----------")
print("item:",items[get_id][0])
print("price:",items[get_id][1])
print("Quantity:",quantity)
total=items[get_id][1]*quantity
print("total bill:",total)
