# Loop
student_list = ['Ibrahim', 'Matthias', 'Bukola','Babatunde','Habbeb']
age_list = [21, 13, 46, 7]

print('Hello, goodmorning', student_list[0])
print('Hello, goodmorning', student_list[1])
print('Hello, goodmorning', student_list[2])
print('Hello, goodmorning', student_list[3])
print('Hello, goodmorning', student_list[4])

# For loop
# Iteration


#     print(each_student)
#     print('Hello, good morning', each_student)

#     print('Hello,good morning', each_student, [+1])

    
for each_student in student_list:
    pos = student_list.index(each_student)
    print(pos+1, 'Hello, good morning', each_student)
    print('')
    
for each_student in student_list:
    pos = student_list.index(each_student)
    print(f'{pos+1}, Hello, good morning, {each_student}')
    print('')

    student_in_tupleclass = ('Sam', 'Matthaias', 'Bukola', 'Babatunde')

print(student_in_tupleclass[1])

for i in student_in_tupleclass:
    print(i)
    
    
student_in_setclass = {'Abeeb', 'Ibrahim', 'Babatunde', 'Bukola', 'Matthaias'}

print(student_in_setclass)

for i in student_in_setclass:
    print(i)
    
student1 = {
    'Name': 'Bukola',
    'Age': 16,
    'Location': 'Oyo',
    'Profession': 'Data Analyst',
    }
student2 = {
    'Name': 'Ibrahim',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student3 = {
    'Name': 'Abbey',
    'Age': 20,
    'Location': 'Port Harcourt',
    'Profession': 'Agba Baller',
    }
student4 = {
    'Name': 'Babatunde',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student5 = {
    'Name': 'Matthaias',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
print('')
print('')

print(student1['Name'], student1['Age'], student1['Location'], student1['Profession'])
print(student2['Name'], student2['Age'], student2['Location'], student2['Profession'])
print(student3['Name'], student3['Age'], student3['Location'], student3['Profession'])
print(student4['Name'], student4['Age'], student4['Location'], student4['Profession'])
print(student5['Name'], student5['Age'], student5['Location'], student5['Profession'])

print(student1)

student1['Friends'] = ['Samuel', 'Matthaias', 'Abeeb']
student1['Age'] = 65
print(student1)

for each_key in student1:
    print(student1[each_key])
    
student_list = [
    student1, 
    student2, 
    student3, 
    student4, 
    student5
    ]

print(student_list)

print('')
print('')
for each_student in student_list:
    print(each_student)
    
# student6_name = input('Enter student name: ')
# student6_age = input('Enter student age: ')
# student6_location = input('Enter student location: ')
# student6_profession = input('Enter student profession: ')

# student6 = {
#     'Name': student6_name,
#     'Age': student6_age,
#     'Location': student6_location,
#     'Profession': student6_profession,
#     }

# print('')
# print('our student list')
# print(student_list)



# Extract the age of all students and find the mean of the total age

# age_list = [16, 35, 20, 35, 35]
# print(age_list)
# for each_student in age_list:
    # pos = age_list.index(each_student)
    # print(pos +1 , age_list(each_student)
        #   print('')

age_list = []
for each_student in student_list:
    #print(each_student['Age'])
    age_list.append(each_student['Age'])

print(age_list)

total_age = 0

for each_age in age_list:
    #total_age = total_age + each_age
    total_age += each_age

print(f'Addition of all the age is {total_age}')
mean_age = total_age / len(age_list)
print(f'The mean of all student age is {mean_age}')

