# def print_hello_world():
#     print("Hello world")
def displayPerson(person_details_list):
    for i in person_details_list:
        print(i)


displayPerson([name, age])

# [a]   TypeError

# [b]   Emma
#       25

# [c]   name
#       age


# 2. What is the output of the following function call

def fun1(num):
    return num + 25


fun1(5)
print(num)

# [a]   25
# [b]   5
# [c]   NameError


# 3. What is the output of the add() function call

def add(a, b):
    return a+5, b+5


result = add(3, 2)
print(result)

# [a]   15
# [b]   8
# [c]   (8, 7)
# [d]   Syntax Error


# 4. Python function always returns a value

# [a]   False
# [b]   True


# 5. Given the following function fun1() Please select all the correct function calls

def fun1(name, age):
    print(name, age)

# [a]   fun1("Emma", age=23)
# [b]   fun1(age =23, name="Emma")
# [c]   fun1(name=”Emma”, 23)
# [d]   fun1(age =23, “Emma”)


# 6. What is the output of the following function call

def fun1(name, age=20):
    print(name, age)


fun1('Emma', 25)

# [a]   Emma 25
# [b]   Emma 20


# 7. Select which is true for Python function

# [a]   A Python function can return only a single value
# [b]   A function can take an unlimited number of arguments.
# [c]   A Python function can return multiple values
# [d]   Python function doesn’t return anything unless and until you add a return statement


# 8. What is the output of the following code

def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)


res = outerFun(5, 10)
print(res)

# [a]   15
# [b]   Syntax Error
# [c]   (5, 10)


# 9. What is the output of the following function call

def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)
    return a


result = outerFun(5, 10)
print(result)

# [a]   5
# [b]   15
# [c]   (15, 5)
# [d]   Syntax Error


# 10. Select which true for Python function

# [a]    A function is a code block that only executes when called and always returns a value.
# [b]    A function only executes when it is called and we can reuse it in a program
# [c]    Python doesn’t support nested function


# 11. What is the output of the following display() function call

def display(**kwargs):
    for i in kwargs:
        print(i)


display(emp="Kelly", salary=9000)

# [a]   TypeError

# [b]   Kelly
#       9000

# [c]   (’emp’, ‘Kelly’)
#       (‘salary’, 9000)

# [d]   emp
#       salary


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!                              !! #
# !! ANSWERS PAST THIS POINT in 3 !! #
# !!                              !! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!                              !! #
# !! ANSWERS PAST THIS POINT in 2 !! #
# !!                              !! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!                              !! #
# !! ANSWERS PAST THIS POINT in 1 !! #
# !!                              !! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #


"""
ANSWERS

1. b
2. c
3. c
4. b
5. a & b
6. a
7. b & c
8. a
9. b
10. a & b
11. d
"""


"""
EXPLANATIONS

1. What is the output of the following displayPerson() function call

def displayPerson(*args):
    for i in args:
        print(i)

displayPerson(name="Emma", age="25")

Explanation:

To accept Variable Length of Keyword Arguments, i.e., To create functions that take n number of Keyword arguments we use **kwargs(prefix a parameter name with a double asterisk ** ).

keyword arguments: fun1(name='Emma', age=23)

Example:

def displayPerson(**kwargs):
    print(kwargs)
displayPerson(name="Emma", age=25)
Use *args to get the variable number of positional arguments.

Example:

def print_numbers(*args):
    print(args)
print_numbers(5, 23, 45, 78)




2. What is the output of the following function call

def fun1(num):
    return num + 25

fun1(5)
print(num)

Explanation:

We must accept the return value of a function into a variable. so we can access it in outside function like this

num = fun1(5)
print(num)



3. What is the output of the add() function call

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

Explanation:

In Python, we can return multiple values from a function. You can do this by separating return values with a comma.





4. Python function always returns a value

False
True


Explanation:

If you do not include any return statement in Python function,
 it automatically returns None. So, a python function always 
 returns a value.

Example:

def display():
    c= 0
    c = 10+20
print(display())
Output:

None




5. Given the following function fun1() Please select all the 
correct function calls

def fun1(name, age):
    print(name, age)


Explanation:

We can pass either use either positional arguments or keyword arguments,
 not both at the same time. If you try to do you will get syntax Error 
 The positional argument follows keyword argument

Possible correct function calls

Positional arguments: fun1('Emma', 23)
keyword arguments: fun1(name='Emma', age=23)
Or, The positional argument must not follow the keyword argument
fun1("Emma", age=23)




6. What is the output of the following function call

def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)


Explanation:

We can specify default values for arguments when defining a function.
 If the value for an argument is missing in the function uses the
  default value.

Example:

def fun1(name, age=20):
    print(name, age)

fun1('Emma')
Output:

Emma 25




7. Select which is true for Python function

A Python function can return only a single value
A function can take an unlimited number of arguments.
A Python function can return multiple values
Python function doesn’t return anything unless and until you add a return statement





8. What is the output of the following code

def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)

res = outerFun(5, 10)
print(res)


Explanation:

Python supports the nested function. We can create a nested 
function to avoid loop or reparation of the code block




9. What is the output of the following function call

def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)
    return a

result = outerFun(5, 10)
print(result)
Question was not answered

Explanation:

Adding multiple return statements doesn’t perform any task. 
Once function execution encountered with the return statement,
 it stops the function execution by returning whatever specified
  by the return statement




10. Select which true for Python function

A function is a code block that only executes when called and always returns a value.
A function only executes when it is called and we can reuse it in a program
Python doesn’t support nested function





11. What is the output of the following display() function call

def display(**kwargs):
    for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000)


Explanation:

To accept Variable Length of Keyword Arguments, i.e., To create functions that take n number of Keyword arguments we use **kwargs(prefix a parameter name with a double asterisk ** ).

keyword arguments: display(emp="Kelly", salary=9000)

This **kwargs collects all passed arguments into a new dictionary, where the argument names are the keys, and their values are the key’s value.

So to get the values we need to iterate the kwargs dictionary like this

Example:

('emp', 'Kelly')
('salary', 9000)



# print_hello_world()

# def return_hello_world():
#     return('hello world')

# return_hello_world()
# print(return_hello_world())
# # print(return_hello_world())

# def blend_items(item1, item2):
#     mixed_items = item1 + item2
#     return mixed_items

# mango_banana_shake = blend_items("mango ", "banana")

# def pour_shake_into_glass(milk_shake):
#     print(f"I poured the {milk_shake} into a glass")

# pour_shake_into_glass(mango_banana_shake)

# def multiply(x,y):
#     result = x * y
#     return(result)


# def is_pelindrome(string):
#     # backwards = string[::-1]
#     # return backwards == string
#     return string[::-1] == string

# word = input('please enter a world to check '.upper())
# if is_pelindrome(word) :
#     print("'{}' is pelindrome".format(word))
# else:
#     print("'{}'is not a pelindrome".format(word))

# answer=multiply(10.5,4)
# print(answer)


# forty_two=multiply(6,7)
# print(forty_two)

# for val in range(1,5):
#     two_times=  multiply(2,val)
#     print(two_times)

def is_pelindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()

# word = input('please enter a world to check ')
# if is_pelindrome(word) :
#     print("'{}' is pelindrome".format(word))
# else:
# #     print("'{}'is not a pelindrome".format(word))
# # Question:
# # write a function where the whole sentence is pelindrome
#     # was it a car, or cat, i saw?

# def pelindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#             string += char

#     print(string)
#     return string[::-1].casefold == string.casefold()
    

# word=input('Please enter your sentence to check ')
# if pelindrome_sentence(word):
#     print("'{}' is pelindrome" .format(word))
# else:
#     print("'{}'This sentence is not pelindrome try again".format(word))

