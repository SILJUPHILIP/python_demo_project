# Guessing game
number = 9

i = 1
while(i <= 3):
    guess = int (input("Guess: "))
    if(guess == number):
        print("you won")
        break
    else:
        print("Sorry you failed")
    i = i + 1