list_of_even_numbers = []
list_of_odd_numbers = []

range_number = input('Enter the range: ')

try:
    range_number = int(range_number)

    for i in range(1, range_number):
        if i % 2 != 0:
            # print(f' {i} - Odd number')
            list_of_odd_numbers.append(i)
        else:
            # print(f' {i} - Even number')
            list_of_even_numbers.append(i)

    # print('Even list -', list_of_even_numbers)
    # print('Odd list -', list_of_odd_numbers)
    total_even = len(list_of_even_numbers)
    total_odd = len(list_of_odd_numbers)
    print('')
    print(f'The total number of even numbers in the list - {total_even}')
    print(f'The total number of odd numbers in the list - {total_odd}')
except:
    print('The range you entered is invalid, plase enter a number')
              
