rivers = {'nile': 'egypt',
          'mississippi': 'U.S.A',
          'amazon' : 'south america'}

for river, countries in rivers.items():
    print(f"The {river.title()} flows through {countries.title()}.")
print(f"\n Rivers in the list ")
for river in rivers.keys():
    print(f"= {river.title()}")
print(f"\n Countries in the list ")
for countries in rivers.values():
    print(f"= {countries.title()}")
