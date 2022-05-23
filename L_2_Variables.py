print("Hello! Welcome to Coffee!")
name = input("What is your name?\n")

if name == "Ben":
    print("You are not welcome here, Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + ", thank you for coming in today!\n\n")

menu = "Black coffee, Espresso, Latte, Cappucino"

print(name + ", what would you like?\n" + menu)

order = input()
price = 8
quantity = input("How many coffees would you like?\n")
total = price * int(quantity)

print("Thank you. Your total is: " + str(total))

print("Sounds good " + name + ", we'll have your "+ quantity + " " + order + " ready in a moment.")




