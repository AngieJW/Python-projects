print("Welcome to the Shopping Cart Program!")
cart = []
prices = []
action =0
while action !=5:
    print("\nPlease select one of the following:")
    print("1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
    action = int(input("Please enter an action: "))

    if action == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        price = float(input(f"What is the price of '{item}'?"))
        prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(cart)):
            item = cart[i]
            print(f"{i+1}. {cart[i]} - ${prices[i]:.2f}")

    elif action == 3:
        j = int(input("Which item would you like to remove?"))
        number = len(cart)
        while j > number:
            print("Sorry, that is not a valid item number.")
            j = int(input("Which item would you like to remove?"))
        cart.pop(j-1)
        prices.pop(j-1)
        print("Item removed.")      

    elif action == 4:
        total = 0
        for i in range(len(cart)):
            total += prices[i]    
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
print("Thank you. Goodbye.")