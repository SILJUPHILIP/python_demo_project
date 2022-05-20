command = ""
while (command != "quit"):
    command = input("> ").lower()
    if(command == "start"):
        print("Car started ready to go...")
    elif (command == "help"):
        print("""
    start - to start the car
    stop - to stop the car
    quit - to exit""")
    elif(command == "stop"):
        print("Car stopped")
    elif(command == "quit"):
        print("exit the program")
        break    
else:
        print("Hey i dont Understand that")
