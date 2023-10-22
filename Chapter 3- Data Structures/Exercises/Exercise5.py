guests = ['Van Gogh', 'Da Vinci', 'Salvador Dali']

# Inviting people
name = guests[0]
print(f"\nHi {name}, would you like to come to dinner at 7:30 tomorrow?")

name = guests[1]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?")

name = guests[2]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?")

# Apology and uninviting one guests
apolo = f"\nSorry but {guests[1]} cant make it, You could invite Alex instead."
print (apolo)

del(guests[1])
guests.insert(1, 'Alex')

name = guests[0]
print(f"\nHi {name}, would you like to come to dinner at 7:30 tomorrow?.")

name = guests[1]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?.")

name = guests[2]
print(f"Hi {name}, would you like to come to dinner at 7:30 tomorrow?.")
