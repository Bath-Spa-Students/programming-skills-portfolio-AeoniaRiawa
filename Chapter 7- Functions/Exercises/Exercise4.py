def make_shirt (size = "L", words = "I <3 python"):
    print(f"The size would be {size}")
    print(f"And it will say {words}")
make_shirt()
print("\nMedium shirt, Default message")
make_shirt(size= 'M')
print("\nCustom size, Custom message")
make_shirt(size = "S", words = "Chungus")