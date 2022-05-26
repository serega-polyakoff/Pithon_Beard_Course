print("Hello! Welcome to Coffee!")
name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?"))
    if evil_status == "Yes" and good_deeds < 4:
      print("You are not welcome here, " + name + "!! Get out!!")
      exit()
    else:
      print("Hello " + name + ", thank you for coming in today!\n\n")

menu = "Black coffee, Espresso, Latte, Cappucino, Frappucino"

print(name + ", what would you like?\n" + menu)

order = input()
price = 8
quantity = input("How many coffees would you like?\n")

if order == "Frappucino":
    price = 13
elif order == "Black coffee":
    price = 3
elif order == "Esspresso":
    price = 5
elif order == "Latte":
    price = 9
elif order == "Cappucino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    price = 0

total = price * int(quantity)

print("Thank you. Your total is: " + str(total))

print("Sounds good " + name + ", we'll have your "+ quantity + " " + order + " ready in a moment.")




