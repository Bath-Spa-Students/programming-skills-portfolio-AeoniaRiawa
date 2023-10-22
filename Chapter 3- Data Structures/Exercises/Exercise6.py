guests = ['Van Gogh', 'Da Vinci', 'Salvador Dali']

# Inviting people
name = guests[0]
print(f"\nHi {name}, would you like to come to dinner at 7:30 tomorrow?")

name = guests[1]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?")

name = guests[2]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?")

# Apology and uninviting one guest
apolo = f"\nSorry but {guests[1]} cant make it, You could invite Alex instead."
print (apolo)

del(guests[1])
guests.insert(1, 'Alex')

# Inviting guests again
name = guests[0]
print(f"\nHi {name}, would you like to come to dinner at 7:30 tomorrow?.")

name = guests[1]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?.")

name = guests[2]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?.")

# Removing 1 guest
print (f"\nSorry but I just found out that there isn't enough room at the table we have to uninvite 1 person.")

name = guests.pop(1)
print(f"Sorry {name}, But it seems like there isn't enough room at the table.")

# Inviting the rest of guests 
name = guests[0]
print(f"\nHi {name}, would you like to come to dinner at 7:30 tomorrow?")

name = guests[1]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?")

# Deleting guests 
del(guests[1])
del(guests[0])
# Making sure there isn't anymore guests
print(f"Number of guests remaining: {guests}")

