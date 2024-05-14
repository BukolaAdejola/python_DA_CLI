
for num in range(1,20):
    if num % 2 == 0:
        print(f'{num} - even')
    elif num % 3 == 0:


        
        print(f'{num} - odd')
    else:
        print(num)

# start_num = input('Enter the start of the range: ')
# start_num = int(start_num)
# end_num = input('Enter the end of the range: ')
# end_num = int(end_num)


# def count_even_odd(start, end):
#     even_count = 0
#     odd_count = 0
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#             print('even_count, odd_count')
            
# even, odd = count_even_odd(start_num, end_num)
# print('number of even numbers:', even)
# print('number of odd numbers', odd)



def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    user_response = input("Enter your choice(1 or 2): ")
    user_response = int(user_response)
    if user_response == 1:
        celsius = input("Enter temperature in celsius: ")
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    elif user_response == 2:
        fahrenheit = input("Enter temperature in fahrenheit: ") 
        fahrenheit = float(fahrenheit)
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice. Please enter 1 or 2.")


