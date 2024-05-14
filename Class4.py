# Control Statement
# Conditional statement: If and else

num1 = 10
# num2 = '10'

user_response = input('Enter your number: ')

if num1 == user_response:
    print('The two numbers are the same')
else:
    print('The two numbers are so different')

    num1 = 10
    num2 = 15

    print('')
    if num1 > num2:
        print('Number 1 is greater than number 2')
    else:
        print('15 is greater than 10')

        num3 = 10
        num4 = 10

    if num3 >=num4 and num1 < num2:
        print('This whole statement is true')
    else:
        print('Equation is not balance')



    if num3 > num4 or num1 < num2:
        print('This is true')
    else:
        print('Equation is not balance')

    if not(num3 == num4): # not False = True
        print('Check negative on Not')
    else:
        print('Equation on NOT not balance ')

    user_age  = input('Enter your age: ')

    print(user_age)
    print(type(user_age))
    # user_age = int(user_age)
    if user_age > 10:
        print('user age greater than 10')
    else:
        print('user age is less than 10')

