for num in range(1, 16):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


student_score = 80


def get_grade(score):
    if 75<= score <= 100:
        print('A1')
    elif 70<= score <= 75:
        print("B2")
    elif 65<= score <=70:
        print("B3")
    elif 60<= score <= 65:
        print("C4")
    elif 50<= score <= 55:
        print("C5")
    elif score >= 50:
        print("C6")
    elif score >= 45:
        print("D7")
    elif score >= 40:
        print("E8")
    else: 
        print("F9")
