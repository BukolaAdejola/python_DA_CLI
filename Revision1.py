
student = 'samuel'
print(student[:3])

student = 'Samuel'
student2 = 'Ibadan'
student3 = 'parach'
student4 = 'Ibrahim'

student_list = [student, student2, student3, student4]

print(student_list[0:2][:3])
# greetings = 'Hello Samuel, welcome to class'
# for each_student in student_list:
#     print(each_student)
#     print(f'Hello {each_student}, welcome to class')
#     print(f'Hello {each_student}, welcome to class, {student2}, pay up')

for each_student in student_list:
    if each_student == 'Ibadan':
        print(f'Hello {each_student}, welcome to class, pay up')

    else:
        print(f'Hello {each_student}, welcome to class')
