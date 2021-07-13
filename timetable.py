# for i in range(1,13):
#     for j in range(1,13):
#         print("{0} times  {1} is {2}" .format(j,i, i*j))
# print('___________________________')

# shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']
# for item in shopping_list:
#     if item == "spam":
#             continue
#     print("Buy " +  item )

shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']
for item in shopping_list:
    if item == "spam":
            break
    print("Buy " +  item )