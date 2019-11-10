leap = int(input('Enter a year to check whether it is a leap year or not: '))
if (leap % 4) == 0:
    if (leap % 100) == 0:
        if (leap % 400) == 0:
            print (leap, ' is a leap year.')
        else:
            print (leap, ' is not a leap year.')
    else:
        print (leap, ' is a leap year.')
else:
    print (leap, ' is not a leap year.')