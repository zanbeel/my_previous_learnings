# dictionary are key values ie
# my_dict={'key1':'value1', 'key2': 'value2'}
# print(my_dict)

# print(my_dict['key1'])

# prices={'apple':1.99 , 'orange':2.99, 'milk':4.99}
# print(prices)
# print(prices['apple'])

# days={'Monday':10,'tuesday':20,'wednesday':30}
# print(days)

# QUESTION: PRINT ALL WORDS START FROM S

# st='print only the words that starts with  s in this sentence'
# for word in st.split():
#     if word[0]== 's':
#         print(word)

# use range to print all the even numbers from 0 to 10

# for i in range(0,10):
#     if i % 2 == 0:
#         print(i)
        
# use list comprehension to list 1 t0 50 number which are divisible by 3

# for i in range (1,51):
#     if i % 3 == 0:
#         print(i)

# print every word of this sentence which has even letters

# st= 'print every word of this sentence which has even number of letters'
# for word in st.split():
#     if len(word)  % 2 ==0:
#         print(word)

#QUESTION:
# Write a program that prints the integers from 1 to 100.
#  But for multiples of three print "Fizz" instead of the number, 
#  and for the multiples of five print "Buzz".
#  For numbers which are multiples of both three and five print "FizzBuzz

# for x in range(1,101):
#     if x % 3 == 0 and x % 5 ==0 :
#         print('FizzBuzz')
#     elif  x % 3 ==0:  
#         print('Fizz')
#     elif x % 5 ==0:
#         print('Buzz')
# else:
#     print(x)
    
# for num in range(1,101):
#     if num%3 == 0 and num%5 ==0:
#         print('FizzBuzz')
#     elif  num%3 == 0:  
#         print('Fizz')
#     elif num%5 == 0:
#         print('Buzz')
# else:
#     print(num)

#QUESIONT:
#Use List Comprehension to create a list of the first letters of every word 
# in the string below:

st = 'Create a list of the first letters of every word in this string'
word=[x[0] for x in st.split()]
print(word) 

