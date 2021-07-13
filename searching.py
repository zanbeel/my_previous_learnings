# shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']

# item_to_find = "spam"
# foud_at = None

#for index in range(6):

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index

# print("item found at postions {} " .format(found_at))

# how to use break in this program(if we do not use it after finding required index it will keep on searching till the end of list)

# shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']

# item_to_find = "spam"
# foud_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# print("item found at postions {} " .format(found_at))

## if the item is not in list then message would be none which does not seems good,
#  so to make it item albatross not found we need to write another it statement

# shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']

# item_to_find = "albatross"
# found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# if found_at is not None:
#     print("item found at postion {}" .format(found_at))
# else:
#     print("{} not found ".format(item_to_find))

## we can write the same result with easy written code:

shopping_list = ['milk' , 'eggs' , 'spam' ,'bread' ,'rice']

item_to_find = "sprout"
found_at = None

if found_at is not None:
    print("item found at postion {}" .format(found_at))
else:
    print("{} not found ".format(item_to_find))


