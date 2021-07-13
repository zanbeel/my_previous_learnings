# for i in range(10):
#         print("i is now {}" .format(i))
# # we will do same thing with while loop
# #when i is greater than zero and exactly divisible by 11

# i = 0
# while i < 10:
#     print("i is now {}" .format(i))
#     i += 1
# for i in range(0, 100, 7):
#      if i > 0 and i % 11 == 0:
#         print(i)      
#         break

# for i in range(0, 100, 7):
#     if i > 0 and 1 % 11 == 0:
#         print(i)
#     break

#ZIP OPERATOR (USED FOR ZIPPING TOGETHER DIFF OBJECTS)

mylist1=[1,2,3]
mylist2=['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

#IN OPERATOR

x=['A','B','C']
'a'  in x
