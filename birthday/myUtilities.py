# three fuctions
# Zoe Jin

# define the function to ask the user for the user’s name
def getName():
    name = input("What's your name?")
    return name


# define the function to ask the user for the user’s birth date
from datetime import date
def getBirthdate():
    m = int(input("What is the month of birth (Format:mm)?"))
    while(m < 1 or m >12):
        m = int(input("Invalid Input!Try again. \nWhat is the month of birth (Format:mm)?"))
              
    d = int(input("What is the day of birth (Format:dd)?"))
    while(d < 1 or d >31):
        d = int(input("Invalid Input!Try again. \nWhat is the day of birth (Format:dd)?"))
        
    y = int(input("What is the year of birth (Format:YYYY)?"))
    while(y < 1 or y >2020):
        y = int(input("Invalid Input!Try again. \nWhat is the year of birth (Format:YYYY)?"))
    result = date(y,m,d)
    return result

# define the function to calcuate the user’s age
today = date.today()
def age(birthday):
    difference = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return difference
    


