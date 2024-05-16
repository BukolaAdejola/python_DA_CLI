for each_numb in range(1, 16):
    print(each_numb)
    if each_numb % 3 == 0 and each_numb % 5 == 0:
        print('FizzBuzz')
    elif each_numb % 3 == 0:
        print('Fizz')
    elif each_numb % 5 == 0:
        print('Buzz')
    else:
        print(each_numb)
    # Question 1 done and dusted
    A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39

score = input('Enter student score: ')
if score.isnumeric():
    score = int(score)

    if score >= 75:
        print(f'student grade is A1 for score of {score}')
    elif score >= 70:
        print(f'student grade is B2 for score of {score}')
    elif score >= 65:
        print(f'student grade is B3 for score of {score}')
    elif score >= 60:
        print(f'student grade is C4 for score of {score}')
    elif score >= 55:
        print(f'student grade is C5 fore score of {score}')
    elif score >= 50:
        print(f'student grade is C6 for score of {score}')
    elif score >= 45:
        print (f'student grade is D7 for score of {score}')
    elif score >= 40:
        print(f'student grade is E8 for score of {score}')
    else:
        print(f' student grade is F9 for score of {score}')


grade_list = ['A1', 'B2', 'B3', 'C4', 'C5', 'D7', 'D7', 'E8', 'F9']
score_list = [75, 70, 65, 60, 55, 50, 45, 40]

student_score = input('Enter student score: ')
if student_score.isnumeric():
    student_score = int(student_score)

    for each_score in score_list:
        index_pos = score_list.index(each_score)
        # print(f'Index of {each_score} is {index_pos}')

        if student_score >= each_score:
            grade = grade_list[index_pos]
            # print(grade)
            # print()
            print(f'student grade is {grade} for score of {student_score}')
            break
        elif student_score < 40:
            print(f'student grade is F9 for score of {student_score}')
            break

else:
    print('You have entered an invalid score')


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
            #print(f' {i} - Even number')
            list_of_even_numbers.append(i)

        # print('Even list -', list_of_even_numbers)
        # print('Odd list -', list_of_odd_numbers)
        total_even = len(list_of_even_numbers)
        total_odd = len(list_of_odd_numbers)
        print('')
        print(f'The total number of even numbers in the list - {total_even}')
        print(f'The total number of odd numbers in the list - {total_odd}')
except:
    print('The range you entered is invalid, please enter a number')
              
