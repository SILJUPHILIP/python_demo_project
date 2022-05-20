
def calculate_weight(mass, gravity):
    return mass * gravity

def calculate_mass(weight, gravity):
     return (weight / gravity)

earth_gravity = 9.807
moon_gravity = 1.62
mars_gravity = 3.721
venus_gravity = 8.87

weight = float(input("Please enter the weight in kgs: "))
body_mass = calculate_mass(weight, earth_gravity)
print("Your body mass is: ", body_mass)

permission = input("Do you want to know your body weight in other planet [Y/N]: ")
if(permission == "Y" or "y" ):
    planet_selection = input("Select your Planet? Moon = [1], Mars = [2], Venus = [3]:")
    if(planet_selection == "1"):
        body_weight_in_moon = calculate_weight(body_mass, moon_gravity)
        print("Your body weight in Moon is: ", body_weight_in_moon)
    elif(planet_selection == "2"):
        body_weight_in_mars = calculate_weight(body_mass, mars_gravity)
        print("Your body weight in Mars is: ", (body_weight_in_mars))
    elif(planet_selection == "3"):
        body_weight_in_venus = calculate_weight(body_mass, venus_gravity)
        print("Your body weight in Venus is: ", (body_weight_in_venus))
    else:print("Wrong Input")
elif(permission == "N" or "n" ):
    print("Thank you visit again")
else:
    print("Wrong input ")
