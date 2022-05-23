
def fibbonocci ():
    number = int(input("enter the first number of your fibbonocci series: "))
    fibanocci_series_length = int(input("enter the length of your fibbonocci series: "))
    fibanocci_series = []
    previous_value = 0
    previous_of_the_previous_value = 0
    index = 1

    while (index <= fibanocci_series_length):
        if (index == 1):
            fibanocci_series.insert(index, number)
            previous_value = number
            previous_of_the_previous_value = 0
        else:
            number = previous_value + previous_of_the_previous_value
            fibanocci_series.insert(index, number)
            previous_of_the_previous_value = previous_value
            previous_value = number
        index = index + 1

    print(fibanocci_series)

fibbonocci()