#1. Hello, you!

#Prompt the user for his name using the input function. Example:

name1 = (input('What is your name? '))
print('Hello ' + name1 + '!')


#Upon receiving his name, you will say hello to him. Example session:


#2. HELLO, YOU!

#Same as the first exercise, but this time print the user's name in ALL CAPS, 
# and also tell them the number of letters in their name. Example session:

name2 = (input('WHAT IS YOUR NAME? '))

print('Hello ' + name2.upper() + '!')

#print('Your name has ' + len(name) + ' in it !')

#3

#What is name? Marty

name3 = (input('WHAT IS YOUR NAME? '))

#What is subject? math

subject1 = (input('What is your favorit subject? '))

#Marty's favorite subject in school is math.

print(name3+"'s" + ' favorite subject in school is ' + subject1)

#4

## make array of all the days in order
## zeroth element is monday, sixth element is sunday
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

## accepts an integer, no strings, if weekday is more than 6 - prints error and returns something else than a week day
def dayNameFromWeekday(weekday):
    if weekday>6:
        print('error');
        return 'an unknown day'
    return days[weekday]


## get keyboard input but convert it to int
nb = int(input('Enter weekday number [0 - 6]: '))
print('\n')

## print the result of the function
print('today is: ' + dayNameFromWeekday(nb))

#5 ASK About this

## make array of all the days in order
## zeroth element is monday, sixth element is sunday
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

## accepts an integer, no strings, if weekday is more than 6 - prints error and returns something else than a week day
def dayNameFromWeekday(weekday):
    if weekday <= 4:
        print('today is: ' + dayNameFromWeekday(nb) + 'GO TO WORK!')
    else:
        print('Today is: ' + dayNameFromWeekday(nb) + 'SLEEP IN')
        
        return 'an unknown day'
    return days[weekday]


## get keyboard input but convert it to int
nb = int(input('Enter weekday number [0 - 6]: '))
print('\n')

#6



# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = int(input('Please enter your Degree\'s in Celsius '))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


#7

bill_amount = float(input('The total bill amount: '))
level_of_service = (input('The level of service, which can be one of the following: good, fair, or bad: '))
good = bill_amount*.20
fair = bill_amount*.15
bad = bill_amount*.10
if level_of_service == good:
    print('The tip Amount is: ' + good)
elif level_of_service == fair:
    print('The tip Amount is: ' + fair)
elif level_of_service == bad:
    print('The tip Amount is: ' + bad)

bill_total = bill_amount + level_of_service

print("Your Total bill amount with tip is: ", bill_total)


#8

#while loop to 10

i = 1

while i <= 10:
    print(i)
    i+=1
else:
    print('The Loop has Ended')

#9

#Write a program that will prompt you for how many coins you want. Initially you have no coins. 
# It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program. Example run:


coin_yes_or_no = int(input('You currently have 0 coins, Would you like another coin? ')) 

while coin_yes_or_no == yes:
    coin_yes_or_no +=1
    print('You have chosen to add coin, you now have ' + coin_yes_or_no)
else:
    print('You have chose to not add a coin !')



coin_add = int(input('Would you like to add another coin'))

if coin_add == yes:
    coin_yes_or_no + coin_add

print('You now have ' + coin_add + 'coins in the bank !')




