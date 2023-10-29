# This chain will check if the value in put is less than or greater than the required values at 'if' and 'elif' statements and will print appropiate responses.
Age = int(input("Please Enter Your Age: "))
if Age < 2:
    print ("You are a baby, How are you using this device?")
elif Age < 4:
    print ("You are a toddler, Go play fornite.")
elif Age < 13: 
    print ("You are a kid, Go play Roblox.")
elif Age < 20:
    print ('You are a teenager, Go have fun in life and make memories.')
elif Age < 65:
    print ("You are a adult, Good luck with everything.")
# If none of them are fufilled the 'else' statement will activate and print the message below.
else: print ("You are a elder, You will pass soon go see your children and grand children.")
# I used the structure like the on the Class_Practice