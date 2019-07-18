def find_max(list_of_numbers):
    maximum = list_of_numbers[0]
    for num in list_of_numbers:
        if maximum < num:
            maximum = num
    return maximum
