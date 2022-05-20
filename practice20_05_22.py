from ast import Not


# logical NOT

price = 5
print( not price > 10)

# if else statement

weight = float(input("Weight: "))
unit = input("kg or lbs: ")
if(unit == "kg"):
    print("Weight in lbs: ", weight / 0.45359237 )
elif(unit == "lbs"):
    print("Weight in kg: ",weight * 0.45359237 )
else:
    print("Invalid Input")

