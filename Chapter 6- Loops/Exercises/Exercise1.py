# A simple print for a welcome
print(" Hi welcome to the toppings section what toppings would you like for your pizza?")
# The value of "asking" will be placed on input command and if the 'if' detects that the user.
# Has inputed the word 'Quit' it would print another value and terminate the loop.
# if not, the loop would continue asking them for toppings till they type "Quit".
asking = "What toppings would like? If you are done simply type 'Quit': "
while True:
    topping = input(asking)
    if topping != 'Quit':
        print(f" You want {topping} on your pizza? Is there anything else?")
    else:
        print(f"\nUnderstood, Please give us a minute while we make your pizza")
        break
    
