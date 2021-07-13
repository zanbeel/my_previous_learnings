# cars=['toyota' , 'mazda' , 'nissan' , 'suzuki' ,'audi']
# print (cars)

# to print items in cap

# cars=['toyota' , 'mazda' , 'nissan' , 'suzuki' ,'audi']
# print (cars[1].title())

#using  f strings to create a message

# cars=['toyota' , 'mazda' , 'nissan' , 'suzuki' ,'audi']
# message= f'I would like to drive {cars[0].title()}'
# print (message)


# Python Expression	Results	Description
# len([1, 2, 3])	3	Length
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
# 3 in [1, 2, 3]	True	Membership
# for x in [1, 2, 3]: print x,	1 2 3	Iteration

# Built-in List Functions & Methods
# Python includes the following list functions −

# Sr.No.	Function with Description
# 1	cmp(list1, list2)
# Compares elements of both lists.

# 2	len(list)
# Gives the total length of the list.

# 3	max(list)
# Returns item from the list with max value.

# 4	min(list)
# Returns item from the list with min value.

# 5	list(seq)
# Converts a tuple into list.

# Python includes following list methods

# Sr.No.	Methods with Description
# 1	list.append(obj)
# Appends object obj to list

# 2	list.count(obj)
# Returns count of how many times obj occurs in list

# 3	list.extend(seq)
# Appends the contents of seq to list

# 4	list.index(obj)
# Returns the lowest index in list that obj appears

# 5	list.insert(index, obj)
# Inserts object obj into list at offset index

# 6	list.pop(obj=list[-1])
# Removes and returns last object or obj from list

# 7	list.remove(obj)
# Removes object obj from list

# 8	list.reverse()
# Reverses objects of list in place

# 9	list.sort([func])
# Sorts objects of list, use compare func if given

# cars=['toyota' , 'mazda' , 'nissan' , 'suzuki' ,'audi']
# message= f'I would like to drive {cars[0].title()}'
# print (message)


# names=['usama','khalid','abdul', 'esbah' ,'salim']
# message=f'{names[0]} is a good muslim'
# print(message)

# to add new item in list

# names.append('kasim')
# print(names)

#Inserting Elements into a List

# names.insert(1,'baboo')
# print(names)

#Removing an Item Using the del Statement
# del names[1]
# print(names)

#Removing/adding an Item Using the pop() Method

# names=['usama','khalid','abdul', 'esbah' ,'salim']
# print(names)
# removed_contact='usama'
# names.remove(removed_contact)
# print(names)
# print(f'{removed_contact} is removed from our whats app group')

# names=['abdul', 'esbah' ,'salim']
# message=f'{names[0]} are invited to dinner'
# message=f'{names[1]} are invited to dinner'
# message=f'{names[2]} are invited to dinner'
# print(message)
# rsvp='abdul'
# names.remove(rsvp)
# print(names)
# print(f'{rsvp} will not be able to make it to dinner')


names=['abdul', 'esbah' ,'salim']
print()
message=f'{names[0]} are invited to dinner'
message=f'{names[1]} are invited to dinner'
message=f'{names[2]} are invited to dinner'
names.append('usman')
print(message)

# printing int in list
# l = [10, 20, 30, 40]
# for i in range(len(l)):
#     print(l[i], end =" ")
# print()
