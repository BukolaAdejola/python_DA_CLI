English = input('Enter English Score: ')
Mathematics = input('Enter Mathematics Score: ')
print(type(English))

if English.isnumeric() and Mathematics.isnumeric():
    English = int(English)
    Mathematics = int(Mathematics)

    if ( English < 0 or English > 100 ) or ( 0 > Mathematics > 100 ):
        print('Student score should be between 0 and 100')
    else:
        if English > 49 and Mathematics > 49:
            print('Student eligible for UI and OAU admission')
        elif English > 49 or Mathematics > 49:
            print('Student is eligible for OAU admission')
        else:
            print('Omo, try again next year')
                    
else:
    print('You have entered invalid value for student scores')   
        
        
        
# try:
#     English_Score = int(English)
#     print(English_Score > 10)
# except:
#     print('Code not working')
    
# if English.isnumeric():
#     print('English score contains numbers only')
#     English_Score = int(English)
#     print(English_Score > 10)

# else:
#     print('English score does not contain numbers only')

'''
Collect a student score and return the corresponding grade
A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39
# Example or eg: PRINT student grade is B3 for score of 67

FIZZBUZZ app
from a list of numbers
for each number
if the number is divisible by 3, print fizz.
if the number is divisible by 5, print buzz.
if the number is divisible by 3 and 5, print fizzbuzz.
if not print the number


'''
Score = 80

Grading_scale = {
'A1' : range (75, 100),
'B2' : range (70, 74),
'B3' : range (65, 69),
'C4' : range (60, 64),
'C5' : range (55, 59),
'C6' : range (50, 54),
'D7' : range (45, 49),
'E8' : range (40, 44),
'F9' : range (0, 39),
}

Student_grade = []
for score_range in grading_scale.item():
    if score in score_range:
        student_grade = Grade
        break

        print(f''The student grade for a score of {score} is: {student_grade}')
          

          list_numb = {
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15  
          }