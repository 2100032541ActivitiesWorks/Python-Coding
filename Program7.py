def leapyear(a):
    if (a % 4 == 0):
        print(a," is a leap year")
    elif (a % 400 == 0):
        print(a,"is a leap year")
    else:
        print(a,"is not a leap year")

x = int(input("Enter the year: "))
leapyear(x)
