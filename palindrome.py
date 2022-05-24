given_number = input("Enter the sequence of number: ")
output = ''
reverse_output = ''
given_number_length = len(given_number)

if (given_number != ''):
    index = given_number_length - 1
    while(index >= 0):
        reverse_output = reverse_output + given_number[index]
        index = index - 1

    if (given_number == reverse_output):
        print("given number ", given_number, " is palindrome")
    else:
        print("given number ", given_number, " is not palindrome")
else:
    print("Invalid input")