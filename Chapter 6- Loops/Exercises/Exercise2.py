# simple intro
print("Hi, Welcome to the cinemas. The ticket pricing is based on your age")
asking = "How old are you dear customer: "
# we placed the "asking" name in a input command 
# age as an integer 
# the system would check if the inputed integer is less than 3 if it is activate first print statement
# if not activate 2nd print statement
# and if the inputted integer surpasses the value of 13 print last print statement
while True:
    age = input(asking)
    age=int(age)
    if age < 3:
        print(f"Oh! it would seem that you are {age} years old. The tickets are on the house!")
    elif age < 13:
        print(f"Oh! it would seem that you are {age} years old. The tickets would be 10$")
    else:print(f"Oh! it would seem that you are {age} years old. The tickets would be 151$")
    break