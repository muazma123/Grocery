fruit = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
vege = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cartprice = 0
cartitems = []

while True:
    print("Select Area to Shop")
    print("(F)ruit")
    print("(V)egetables")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()

    if len(area) > 1:
        area = area[0]

    if area == "f":
        print("Fruit Section")
        print("(A)pples")
        print("A(v)ocado")
        print("(B)anana")
        print("(K)iwifruit")
        print("(O)ranges")
        print("(G)o Back")
        fruit_choice = input("Enter Fruit letter: ").lower()

        if len(fruit_choice) > 1:
            fruit_choice = fruit_choice[0]

        choices = ["a", "v", "b", "k", "o", "g"]

        if fruit_choice not in choices:
            print("Selection Error")
            continue
        elif fruit_choice == "a":
            fruit_find = fruit.index("apples")
        elif fruit_choice == "v":
            fruit_find = fruit.index("avocado")
        elif fruit_choice == "b":
            fruit_find = fruit.index("banana")
        elif fruit_choice == "k":
            fruit_find = fruit.index("kiwi")
        elif fruit_choice == "o":
            fruit_find = fruit.index("oranges")
        else:
            continue

        fruit_price = float(fruit[fruit_find + 1])
        fruit_amount = int(input(f"How many {fruit[fruit_find]} do you want: "))
        fruit_cost = fruit_price * fruit_amount

        cartprice += fruit_cost
        cartitems.append(fruit[fruit_find])

        print(f"Cost so far = {cartprice}")
        print(f"Cart items = {cartitems}")

    elif area == "v":
        print("Vegetable Section")


    elif area =="d":
        print("Delicatessan")


    else:
        break
