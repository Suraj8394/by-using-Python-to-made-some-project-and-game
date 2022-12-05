#class=29

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? \n"))

if height>=120:
    print("You can ride rollercoaster\n")
else:
    print("Sorry, You have grow taller before you can ride.\n")


#class=30

#modula operation(remainder)
print(7%3)
print("welcome to my world\nplease check any number have even or odd")
num=int(input("Enter any number:-"))
if num%2==0:
    print("This is an Even Number")
elif num%2!=0:
    print("This is an Odd Number")
else:
    print("Bye Bye")


#class=31

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))

if height>=120:
    print("You can ride the roolercoaster")
    age=int(input("What is your age? "))
    if age>=18:
        print("Please pay $12.")
    elif 12<=age<=18:
        print("Please pay $7")
    else:
        print("Please pay $5")
else:
    print("Sorry, You have to grow taller before you can ride.")


#class=32

height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=round(weight/height**2, 2)
if bmi<=18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif 18.5<=bmi<=25:
    print(f"Your BMI is {bmi}, you are a normal weight")
elif 25<=bmi<=30:
    print(f"Your BMI is {bmi}, you are overweight")
elif 30<=bmi<=35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")


#class=33

#leap year
year=int(input("Which year do you want to check: "))
if year % 4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


#class=34


#add photo price
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0

if height>=120:
    print("You can ride the roolercoaster")
    age=int(input("What is your age? "))
    if age>=18:
        bill=12
        print("Adult tickets $12.")
    elif 12<=age<=18:
        bill=7
        print("Youth tickets $7")
    else:
        bill=5
        print("Child tickets $5")

    wants_photo=input("Do you want a photo taken? yes or no : ")
    if wants_photo=="yes":
        bill+=3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")


#class=35

#add extra bill price
print("Welcome to Python Pizza Deliveries!")
pizza_size=input("What Size Pizza do you want? S, M AND L : ")
add_pepperoni=input("Do you want pepperoni? yes or no : ")
extra_chesse=input("DO you want extra cheese? yes or no : ")
bill=0
if pizza_size=="S":
    bill += 15
elif pizza_size=="M":
    bill += 20
elif pizza_size=="L":
    bill += 25
else:
    bill+=25

if add_pepperoni=="yes":
    if pizza_size=="S":
        bill+=2
    elif pizza_size=="M"or"L":
        bill+=3
    else:
        bill+=3

if extra_chesse=="yes":
        bill+=1

print(f"Your final bill is ${bill}")


#class=36

#uses of logic
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0

if height>=120:
    print("You can ride the roolercoaster")
    age=int(input("What is your age? "))
    if 18<=age<45:
        bill=12
        print("Adult tickets $12.")
    elif 12<=age<=18:
        bill=7
        print("Youth tickets $7")
    elif age>=45 and age<=55:
        print("Everthing is going to be ok. Have a free ride on us!")
    else:
        bill=5
        print("Child tickets $5")

    wants_photo=input("Do you want a photo taken? yes or no : ")
    if wants_photo=="yes":
        bill+=3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")


#class=37

#love calculator
print("Welcome to the love Calculator")
name1=input("What is your name? \n")
name2=input("What is their name? \n")

combined_string=name1+name2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true= t+r+u+e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love=l+o+v+e

love_score = int(str(true)+str(love))

print(love_score)

if (love_score<10) or (love_score>90):
    print(f"Your love score is{love_score}, you go together like")
elif (love_score>+40) and (love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


#class=38

#tresure island GAME
print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1=="left":
    choice2=input('you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose?").lower()
        if choice3=="red":
            print('It\'s a room full of fire. Game Over')
        elif choice3=="yellow":
            print("You found treasure! You Win!")
        elif choice3=="blue":
            print("You enter a room of beasts. Game Over")
        else:
            print('You chose a door that doesn\'t exist. Game Over')
    else:
        print("You got attached by an angry trout. Game Over.")
else:
    print(" You fell into a hole. Game Over")