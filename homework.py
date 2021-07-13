
# Print First 10 natural numbers using while loop
i = 0
while i <= 10:
    print(i)
    i = i + 1

# Print the following pattern

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# for i in range (6):
#     print( 'iteration' + str(i) + ':')
#     for j in range (i):
#         print(j+ 1, end = " ")
#     print()

for i in range(6):
    for j in range(i):
        print(j + 1, end = " ")
    print()

# Accept number from user and calculate 
# the sum of all number from 1 to a given number


num = int(input(' Please enter a number'))
i = 0
j = 0
while i < num:
    i = i + 1
    j = j + i
    print(j)

    
# Exercise 4: Print multiplication table of a given number

num = int(input(' Please enter a number'))
i =  0
while i in range(num):
    print(num * i)
    i = i + 1

# Exercise 5: Given a list, iterate it, and display numbers 
# divisible by five, and if you find a number greater than 150, 
# stop the loop iteration.

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in (list1):
    if i % 5 == 0:
        print(i)
        if i >= 150:
            break

# Exercise 6: Given a number count the total number of digits
#  in a number For example, the number is 75869,
#   so the output should be 5.

num = int(input( ' write a number to count'))
i = str(num)
for i in str(num):
    print(len(str(num)))
    break

num = int(input( ' write a number to count'))
i = str(num)
print(len(str(num)))

# Print the following pattern using for loop
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


for i in range(5,0,-1):
    for j in range (5,0,-1):
        if j <= i:
            print(i, end =" ")
            i = i - 1
    print()

# Exercise 8: Reverse the following list using for loop

list1 = [10, 20, 30, 40, 50]
j= list1
for i in reversed(j):
    print(i)

# Exercise 9: Display numbers from -10 to -1 using for loop

    
num = 0
for num in range (-10,0,1):
    print(num)

# Exercise 10: Display a message “Done” after successful execution
#  of for loop

for i in range (5):
    print(i)
print('Done!')

# Exercise 11: Write a program to display all prime numbers
#  within a range

start =  int(input('Please enter the first number \n'))
end = int(input('Please enter the first number \n'))

for num in range (start,end + 1):
    # start from 2, if starting number is > 1 then go to for loop:
    if start > 1:
        # value of i will start from 2:
        for i in range ( 2, num):
            # if every number(starting range to end + 1) in loop is divisible 
            # without remainder: 
            if num % i == 0:
                # stop loopingwith break and go back to outer, for loop:
                break
            # otherwise print the message
            else:
                print( i, 'is prime number')

#Exercise 12: Display Fibonacci series up to 10 terms
#0  1  1  2  3  5  8  13  21  34

value = int(input('please enter the number '))

v1 = 0
v2 = 1
for num in range(value):
    print (v1)
    # step 1) value of (v1) variable is stored in  new variable called (tempv)
    tempv = v1
    # step 2) value of second variable(j) is stored in first variable (tempv)
    v1 = v2
    # step 3) second value(v2) is stored in variable v1(tempv)to start counting 
    # backwards i.e (0,1,1,2,3)
    v2 = tempv + v2
    

# Exercise 14: Reverse a given integer number
# Given: 76542

j = 76542
# since int objects are not reversible we will make variable j 
# into string 
for i in reversed(str(j)):
    print(i, end = ' ')

# Exercise 15: Use a loop to display elements from a given list that
# are present at even index positions
# Given:

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in list[1::2]:
    print(i, end = " ")

# Exercise 16: Display the cube of the number up to a given integer

i =  6
for i in range(1,i + 1):
    print(i*i*i)

