# The list with items and the list that is emtpy to be filled with items from the other list.
Sandwich_orders = ['Onion', 'Tuna', 'Chicken', 'Cheese']
Finished_sandwiches = []
# Okay im gonna be honest i searched this one up becaue i have no idea.
# But i didn't just copy paste it. i did try to understand.
# so from what i got .pop means that we are gonna remove 1 value from Sandwhich_orders.
# And for us to place that removed value we are going to use .append which adds a item to a list
while Sandwich_orders:
    order = Sandwich_orders.pop()
    print(f" Currently making {order} sandwhich please hold.")
    Finished_sandwiches.append(order)
print(f"\n Proccessing...yummy?")
# Now that the items are transferred we just make so for every bread that is in the finished_sandwich list
# i will print the sandwhich is complete
for breaders in Finished_sandwiches:
    print (f"The {breaders} sandwhich is complete")


