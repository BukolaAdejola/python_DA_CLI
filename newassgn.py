

def count_even_odd(start, end):
    even_count = 0
    odd_count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            print('even_count, odd_count')
start_num = input('Enter the start of the range: ')
start_num = int(start_num)
end_num = input('Enter the end of the range: ')
end_num = int(end_num)

even, odd = count_even_odd(start_num, end_num)
print('number of even numbers:', even)
print('number of odd numbers', odd)
for num in range(1,20,2):
    print(num)

