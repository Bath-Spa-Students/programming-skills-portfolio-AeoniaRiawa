pets=[]
pet = {
    'Kind':' Dog',
    'Name':' Bark',
    'Owners': ' John',
    'Status': 'Dead'
}
pets.append(pet)
pet = {
    'Kind':' Cat',
    'Name':' Kat',
    'Owners': ' Cait',
    'Status': 'Dead'
}
pets.append(pet)
pet = {
    'Kind':' Turtle',   
    'Name':' Speed',
    'Owners': ' Crash',
    'Status': 'Alive'
    }
pets.append(pet)
print (f"\t{pets}")

# OR

for pet in pets:
    print(F"Info about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")