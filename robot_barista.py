#Let's start a coffee shop together!! 
# We're going to build a coffee shop using some new python programming concepts!!

#Let's build robot Barista!!

print("Hello, Welcome to Rishi's Cafe!!!!!!")
name = input("What is your name?: ")

print("\nHello , " + name + ", Thank you so much for coming in today.\n") 

menu = "Black coffee, Espresso, Latte, Cappuccino."

print(name + ", What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()
price = 40

Quantity = input("\nHow many coffee would you like: ") 
total = price * int(Quantity)

print("Thank You. Your total is: " + str(total) + " rupees")

print("\nsounds good " + name + ", we'll have your " + Quantity + " " + order + " Ready for you in moment." )
