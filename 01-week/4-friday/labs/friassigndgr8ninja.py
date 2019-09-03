#1 Sum of Numbers

numbers = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

#2 Largest Number

list1 = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10]
list1.sort()
print("The Largest number in the list is: ", list1[-1])

#3 Smallest Number

list1 = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10]
list1.sort()
print("The Largest number in the list is: ", min(list1))

#4 Even Numbers

# list of numbers 
list1 = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10]
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print('This is a list of even numbers: ', list1[num]) 
      
    # increment num   
    num += 1

#5 Positive Number

# list of numbers 
list1 = [11, -21, 0, 45, 66, -93, 58, 23, -67, 2013, -1014] 
  
num = 0
  
# using while loop      
while(num < len(list1)): 
      
    # checking condition 
    if list1[num] > 0: 
        print('This is a list of positive numbers: ', list1[num]) 
      
    # increment num  
    num += 1

#6 Positive numbers II

list1 = [11, -21, 0, 45, 66, -93, 58, 23, -67, 2013, -1014] 
  
num = 0
  
# using while loop      
while(num < len(list1)): 
      
    # checking condition - ASK 
    if list1[num] >= 0: 
        print('This is a list of positive numbers: ', list1[num]) 
      
    # increment num  
    num += 1

#7 Multiply a List


def multiplylist(list1):

    result = 1

    for x in list1:
        result = result * x
    return result

list1 = [1, 2, 3, 4, 5] 

print("This is a list of multiplied numbers: ", multiplylist(list1))

#8 Multiply Vectors - ASK 

# matrix
X = [2, 4, 5]
Y = [2, 3, 6] 
    

# Result Variable for Matrices

result = []

# iterate through rows of X
for i in range(0, len(X)):

       # iterate through rows of Matrix
    num = X[i] * Y[i]

    result.append(num)
    print(result)
    


#9 Matrix Addition I

#  matrix
X = [2, -2]
Y = [5, 3] 
    

# Result Variable for Matrices

result = []

# iterate through rows of X
for i in range(0, len(X)):

       # iterate through rows of Matrix
    num = X[i] + Y[i]

    result.append(num)
    print(result)

       
#10 Matrix Addition II

#  matrix
X = [2, -2, 2]
Y = [5, 3, 2]
Z = [4, 8, 3]
    

# Result Variable for Matrices

result = []

# iterate through rows of X
for i in range(0, len(X)):

       # iterate through rows of Matrix
    num = X[i] + Y[i] + Z[i]

    result.append(num)
    print(result)


#11 De-dup

list1 = ['blue','violet','red','orange']

nodupes = []

for name in list1:
    if name not in nodupes:
        nodupes.append(name)


print(nodupes)



# 1. loops Assignment - Friday 08/30/2019

for x in range(1,11):
    print (x)

# 2. N to M 

n = int(input('Enter a number to print upt to 100 '))

print(list(range(1,n+1)))

# 3. Odd Numbers to Print

print("using start, stop, and step arguments in Python range() function")
print("Printing All odd numbers between 1 and 10 using range()")
for i in range(1, 10, 2):
    print('' , i, end=',  ', )
    print('\n')

    

#4 Print a Square
# Python Program to Print Square Star Pattern
 
side = int(input("Please Enter any Size of a Square  : "))

print("Square Star Pattern") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()

#5 Print a Square II

#This is also taken care of in the above, parameters simply have to be set restricting the amount of stars

#6 # Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()

# 7 Print a Triangle

print("Program to print half pyramid: ");
rows = input("Enter number of rows ")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")


#8 Print a Triangle II


print("Print full Triangle pyramid using stars ")
rows = input("Enter the Number of Rows in this Triangle: ")
rows = int(rows)
m = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")

#9 Multiplication Tables

print('This is a Multiplication Table from 1 thru 10')

row =  int(input("Enter the number you would like to see a multiplication table thru 10 for: "))

for i in range(1, 11):
    print(row, 'x', i, '=', row * i)



# Monday review for Friday Assignment