#to check if the input year is leap or not
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is leap")
        else:
            print("The year is not leap")
    else:
        print("The year is leap")
else:
    print("The year is not leap")
    