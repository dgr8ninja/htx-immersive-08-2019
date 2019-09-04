#1. MadLib Function

def two_arguments(name, subject):
    return name, subject

print(two_arguments('Damon', 'Biology'))

# 2 - 3 Celsius to Fahrenheit conversion


# def convert_temp(scale=None, temp=None):
#     if scale == "F":
#         return(temp - 32.0) * (5.0/9.0)
#     elif scale == "C":
#         return(temp * (9.0/5.0)) + 32.0
#     else:
#         print("Needs to be (F) or (C)!")
#         return

# scale = input("Select (F) or (C): " )
# temp = int(input("What is the temperature: " ))
# m = convert_temp(scale, temp)
# print(temp, "degrees", scale, "is", m, "degrees", scale)

#4. is_even function

def is_even(num):
    num = (int(input("Please input a whole number: ")))
    if num == num[::-1]:
        return True
    else:
        return False





 
    




