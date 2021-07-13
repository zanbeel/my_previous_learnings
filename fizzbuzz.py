# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

# for num in range(1,101):
   
#     if num % 3 == 0 and num % 5 == 0:
#         print ('fizzbuzz')
#     elif num % 3 == 0:
#         print('fizz')
#     elif num % 5 == 0:
#         print('buzz')
#     else:
#         print('num')

# Solved with function

def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 ==0):
        return 'fizzbuzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input
print(fizzbuzz(7))

def customers(name,number_of_apples=10):
    print('Hello ' + name )
    print('we have ' + str(number_of_apples)+ ' apples in stock')


customers('greg')
customers('brown',7)
customers('kevin',9)

def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(40,60))

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print(' I did not find and fruit here')
print(myfunc(fruit='apple'))

