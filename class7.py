# Quick tasks
# Create a list of number values
# write a function that adds all the numbers in the list together

list_of_numbers = [1, 2, 5, 2, 6, 34, 6, 34 ]

def addNumbersInList():
    #result + sum(list_of_numbers)

    result = 0
    for each_number  in list_of_numbers:
        result = result + each_number

    print(result)

addNumbersInList()


student1 = {
    'name': 'Bukola',
    'location': 'Ibadan',
    'age': '16',
    'profession': 'programmer',
    'friends': ['Matthias', 'Babatunde']
}

student2 = {
    'name': 'Matthias',
    'location': 'Lagos',
    'age': '47',
    'profession': 'Technologist',
    'friends': ['Matthias', 'Ibrahim']
}

student3 = {
    'name': 'Ibrahim',
    'location': 'Oyo',
    'age': '49',
    'profession': 'Business',
    'friends': ['Samuel', 'Babatunde']
}

student4 = {
    'name': 'Babatunde',
    'location': 'Abuja',
    'age': '28',
    'profession': 'Doctor',
    'friends': ['Matthias', 'Bukola']
}

student_list = [
    student1, 
    student2, 
    student3, 
    student4, 
    ]
# write a function that adds the age of all students together.

# list_of_age = [16, 47, 49, 28]

# def addagelist():
    
#     result = 0
#     each_age = int(each_age)
#     for each_age in student_list:
#         print(sum(student_list['age']))
        

# addagelist()

python_student_list = [
    student1, student2, student3, student4
]


def addStudentsAge(all_students): # parameter/requirement
    # result = 0
    # for each_student in all_students:
    #     print(each_student['age'])
    #     result +=  int(each_student['age'])

    #     print(result)

    age_list = []
    for each_student in all_students:
        age_list.append(int(each_student['age']))

    print(sum(age_list))

addStudentsAge(python_student_list) # Argument

# default arguments

def showprofile(name, age, location='parach', *friends):

    print(f"""
          The name of the student - {name}
          Student is {age} years old.
          Student is currently in {location}
          
          """)  #f' ' format - to pass a variable into a string
    for friend in friends:
        print(f'{name} has a friend called {friend}')

showprofile(
            student1['name'],
            student1['age'],
            student1['location'],
            student1['friends']

        )
    
'''
create a list of at least 5 states and capital. From  user option 1-4
perform
1. Read - display all states and capital
2. Create - User can add a sate and capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital
'''

def sh(name, location='Parach'):

    print(f'Student name is  {name}, student lives at {location}')

    sh('Bukola', 'Lagos')
    sh('Matthias')
