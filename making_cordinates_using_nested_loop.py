for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# making F with nested loop

numbers = [5, 2, 5, 2, 2]
for value in numbers:
    output =''
    for number in range(value):
        output += 'x'
    print (output)
    