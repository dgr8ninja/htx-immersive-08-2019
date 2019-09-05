#1. MadLib Function

def two_arguments(name, subject):
    return name, subject

print(two_arguments('Damon', 'Biology'))

# 2 - 3 Celsius to Fahrenheit conversion


def convert_temp(scale=None, temp=None):
    if scale == "F":
        return(temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return(temp * (9.0/5.0)) + 32.0
    else:
        print("Needs to be (F) or (C)!")
        return

scale = input("Select (F) or (C): " )
temp = int(input("What is the temperature: " ))
m = convert_temp(scale, temp)
print(temp, "degrees", scale, "is", m, "degrees", scale)

#4. is_even function

def is_even(number):
    return (number %2 == 0)



#5 is_odd function

def is_odd(number):
    return not is_even(number)

#6 Only-Even Function
def only_evens(list_of_numbers):
    result = []
    for number in list_of_numbers:
        if is_even(number):
            result.append(number)
        return result
        
        
only_evens([11, 20, 42, 97, 23, 10])

#7 Only_Odds Function

def is_odd(number):
    return not is_even(number)

#6 Only-Even Function
def only_oddss(list_of_numbers):
    result = []
    for number in list_of_numbers:
        if is_odd(number):
            result.append(number)
        return result
        
        
only_evens([11, 20, 42, 97, 23, 10])




 
    




