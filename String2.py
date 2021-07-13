# how to use sbstr


parrot = "Norwegian Blue"

print(parrot)

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

# how to slice words
# parrot = "Norwegian Blue"
# find Norweg

print(parrot[0:6])
# start from begining and after : shows characters
print(parrot[:6])
# will produce first 6 characters
print(parrot[6:])
# Get whole string
print(parrot[:])

string= "abcdefghijklmnopqrstuvwxyz"
print(string)
print(string[3])
print(string[-4])


parrot = "Norwegian Blue"
print (parrot)
print(parrot[-14:-8] )

print(parrot[-4:-2]) # ????
print(parrot[-4:12])  #???


# TOPIC : # step value of Slice
# How to get NRE from  "Norwegian Blue"
# Slice starts at index position 0
# it extends up to (but not including) postion 6
# we step through the sequence in steps of 2(picking letters after every two numbers)

print(parrot[0:6:2])

print(parrot[1:9:3]) # oea
print(parrot[2:14:4]) #rib

number = "9,223;372:036 854,775;807"
seperators = number[1: :4]
print(seperators)


values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
