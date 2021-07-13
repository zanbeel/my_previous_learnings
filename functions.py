# mylist=[1,2,3]
# mylist.append(4)
# print(mylist)

# mylist.pop()
# print(mylist)

# help(mylist.count) 
# print(mylist)


# def say_hello(name='default'):
#     print(f'hello {name}')
#     say_hello()

# def add_num(num1,num2):
#     return num1+num2
# result=(add_num(10,20))
# print(result)

# def return_results(a,b):
#     return a+b
# result=return_results(10,20)
# print(result)
    

# def check_even_list(num_list):
#     for number in num_list:
#         if number  %2 == 0:
#             return True
#         else:
#             pass 
#     return False

# print(check_even_list([1,3,7]))

# def guess(num):
#     #place holder for even number
#     even_number=[]
#     # then we will go ove the number list
#     for number in  num:
#         if number %2 ==0:
# #if I attach to even number I will append it to my list
#             even_number.append(number)
# # and before returning even numbers we will loop through 
# # evey number in the list
#     else:
# #         pass
# # # and then we will print even number
# #     return even_number

# # print(guess([1,2,3,4,5,6,7,]))

# example=[1,2,3,4,5,6,7,8,9]
# from random import shuffle 
# result=shuffle(example)
# print(result)
# #does not produce any result

# def shuffle_list (mylist):
#     shuffle(mylist)
#     return(mylist)

# result=shuffle_list(example)
# print(result)

# mylist=['','O','']
# shuffle_list(mylist)

# def player_guess():
#         guess= ''
#         while guess not in ['0','1','2']:
#             guess= input("pick a number: 0,1, or 2 ")
#         return int(guess)
# myindex= player_guess()

# print(myindex)

# def check_guess(mylist,guess):
#     if mylist[guess] == 'O':
#         print("correct!")
#     else:
#         print("wrong guess!")
#         print(mylist)

# #initial list
# mylist =['','O','']
# # shuffle list
# mixedup_list = shuffle_list(mylist)
# #user guess
# guess=player_guess()

# #check guess
# check_guess(mixedup_list,guess)

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number
#     return(total)
# print(multiply(2,3,4,5))

# DICTIONARY

def user_name(**user):
    print(user['id','name','age'])

print(user_name(id=1,name='john',age=24))