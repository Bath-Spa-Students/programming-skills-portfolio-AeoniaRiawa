Sandwich_orders = ['Pastrami','Pastrami','Pastrami','Onion', 'Tuna', 'Chicken', 'Cheese']
Finished_sandwiches = []
# The entire program is just a copy paste of the previous exercise. For explanations check that one out
# The only difference in this one is that there is a item in a list that we will remove with the command .remove()
print("Dear customers, We are out of pastrami all orders of Pastrami will be cancelled")
while 'Pastrami' in Sandwich_orders:
    Sandwich_orders.remove('Pastrami')
    
while Sandwich_orders:
    order = Sandwich_orders.pop()
    print(f" Currently making {order} sandwhich please hold.")
    Finished_sandwiches.append(order)
print(f"\n Proccessing...yummy?")

for breaders in Finished_sandwiches:
    print (f"The {breaders} sandwhich is complete")