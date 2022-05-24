number = int (input("enter a number: "))
output = 1
for value in range(number):
    if (number > 0):
      output = output * (value + 1)
      
    else:
        print("Enter a valid number")

print(output)
