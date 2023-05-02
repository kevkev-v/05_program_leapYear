# This program will tell the user if a given year is a leap year

# Formula -- The way you find out if a number is a leap year is --
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year}, is a leap year")    
        else:
            print(f"The year {year}, is not a leap year")            
    else:
        print(f"The year {year}, is a leap year")
else:
    print(f"The year {year}, is not a leap year")