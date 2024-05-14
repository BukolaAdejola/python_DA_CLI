#Integers
num1 = 64
num2 = 304

# Operator
# Arithmetic operators

print(num1 + num2) # addition
print(num1 - num2) # subtraction
print(num1 / num2) # division
print(num1 * num2) # multiplication

print(num1 % num2) # % modulus : returns the remainder
print(num1 ** num2) # ** Exponential : num1 raise to the power num2
print(num1 // num2) # // Floor Division

n1 = 5
n2 = 2

print('Divide 5 by 2')
print(n1/n2)
print(n1 % n2)


print('Exponential')
n1 = 5
n2 = 3
print(n1 ** n2)

print('Floor division')
print(type('Floor division'))
n1 = 125
n2 = 17

result1 = n1 / n2
print(result1)
print(type(result1))

result2  = n1 // n2
print(result2)
print(type('result2'))

print('complex')
comp = 12e5
print(comp)
print(type(comp))

#Boolean
# We use boolean for comparism
# Comparism Operators
tr = True
fl = False
n1 = 8
n2 = 5
print(n1 > n2)
print(type(n1 > n2))


# Python Collection/Array
# List

student_list = ['Ibrahim', 'Matthias', 'Bukola','Babatunde','Habbeb']
age_list = [21, 13, 46, 7]
print(student_list)
print(len(student_list))
print(student_list[1])
print(student_list [1][4:])

student_list.append('Samuel') # Adding new item to the end of a list[]
print(student_list)
student_list.pop() # Removes the last item from a list
print(student_list)
student_list.pop(2) #Removes an item at a position in the list
print(student_list)
student_list.sort() # Arranges in a sequence
age_list.sort() # Arranges in a sequence
print(student_list)
print(age_list)
student_list.reverse() # Arranges in reverse sequence
print(student_list)


student_list.clear() # Removes all the element from the list
print(student_list)
student_list = ['Ibrahim', 'Matthias', 'Bukola','Babatunde','Habbeb']
print(student_list)
student_list.count("Bukola") # Returns the number of elements with the speified value
print (student_list)
student_list.copy()  # Returns a copy of the list
print(student_list)
student_list.insert(2, "Grace") # Add an element at the specified position
print(student_list)
student_list.remove("Ibrahim") # Removes the first item with a specified value
print(student_list)
student_list.index("Babatunde")  # Returns the index of the first element with d specified value
print(student_list)


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. it comes in pairs (key and Value)

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
    
student6_name = input('Enter student name: ')
student6_age = input('Enter student age: ')
student6_location = input('Enter student location: ')
student6_profession = input('Enter student profession: ')

student6 = {
    'Name': student6_name,
    'Age': student6_age,
    'Location': student6_location,
    'Profession': student6_profession,
    }

print('')
print('')
print(student6)




