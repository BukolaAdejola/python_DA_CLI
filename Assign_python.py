# Draw a right angle triangle using the print statement

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

            for row in range(1, totalrow+1):
                # display space
                for space in range(1, (totalrows-row)+1):
                    print(" ", end="")

                    #display *
                    for symbol in range(1,row+1):
                        print("*", end="")

                        print()