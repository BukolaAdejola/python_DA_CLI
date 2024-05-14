person3 = 'Ibrahim'
print(person3)
print(person3.casefold()) # converts string into lowercase
print(person3.capitalize()) # converts the first character to upper case
print(person3.center()) # returns a centred string
print(person3.count()) # returns the number of times a specified value occured in a string
print(person3.encode()) # returns an encoded version of the string
print(person3.find()) # searches the string for a specified value and returns the position of where it is found
print(person3.endswith()) # returns true if the string ends with specified value
print(person3.format()) # formats specified value in a string
print(person3.format_map()) # formats specified value in a string
print(person3.expandtabs()) # sets the tab size of the string
print(person3.isalnum()) # returns true if all values in the string are alphanumeric
print(person3.index()) # searches the string for a specified value and returns the position of where it was found



rows = int(input("please enter the total number of rows :"))
ch = input("Please enter any character :")

print("Mirrored Right triangle star pattern")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if (j <= rows - i):
            print(' ', end = ' ')
        else:
            print('%c' %ch, end = ' ')
            print()

            totalrows = int(input("enter the number of rows : " ))

            for row in range(1, totalrows+1):
                # display space
                for space in range(1, (totalrows-row)+1):
                    print(" ", end="")

                    #display *
                    for symbol in range(1,row+1):
                        print("*", end="")

                        print()


print(person3)
print(person3.casefold()) # converts string into lowercase
print(person3.capitalize()) # converts the first character to upper case
print(person3.center()) # returns a centred string
print(person3.count()) # returns the number of times a specified value occured in a string
print(person3.encode()) # returns an encoded version of the string
print(person3.find()) # searches the string for a specified value and returns the position of where it is found
print(person3.endswith()) # returns true if the string ends with specified value
print(person3.format()) # formats specified value in a string
print(person3.format_map()) # formats specified value in a string
print(person3.expandtabs()) # sets the tab size of the string
print(person3.isalnum()) # returns true if all values in the string are alphanumeric
print(person3.index()) # searches the string for a specified value and returns the position of where it was found


student_list = ['Ibrahim', 'Matthias', 'Bukola','Babatunde','Habbeb']
print(student_list)


print('|\ ')
print('| \ ')
print('|  \ ')
print('|   \ ')
print('|    \ ')
print('|     \ ')
print('|______\ ')