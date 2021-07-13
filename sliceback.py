letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)


backwards = letters[-12:-9]
print (backwards)

backwards = letters[-9:-1]
print (backwards)

print(2+2)
# print(2 +" 2 ")
print("2"+"2")
print('hello there'[9])
      #012345678910


backwards = letters[-10:-1]
print (backwards)

backwards = letters[-10:-13:-1]
print(backwards)

backwards = letters[14:17]
print(backwards)

backwards = letters[10:5:-1]
print(backwards)

# slice a string to produce edcba

backwards = letters[4::-1]
print(backwards)

# last 8 characters in reverse order
# start from 8, move forward index 9 
# and do not include 9, go backward by one step

backwards = letters[25:-9:-1]
print(backwards)

#  Slice that produces the characters qpo

# we start from index 16, we are extending backwards
#upto but not including index 13

backwards = letters[16:13:-1]
print(backwards)


#This will produce the same result

backwards = letters[-10:-13:-1]
print(backwards)
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_array=['a', 'b', 'c', 'd', 'e', 'f', [1, "John", "Doe"], 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#'vutsrq'

xyz=alpha[21:15:-1]
print(xyz)

print()

xyz=alpha[-5:-11:-1]
print(xyz)



# "qomkig"

xyz=alpha[16:5:-2]
print(xyz)

xyz=alpha[-10:-21:-2]
print(xyz)

xyz=alpha[0]
print(xyz)

xyz=alpha[4]
print(xyz)
xyz=alpha_array[6]
print(xyz)
print()


s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))

s='foobar'
print (s [::-5])

s='foobar'
print(s[::-1] [-1] + s[-1])

s='foobar'
print(s[0] + s[-1])

print()
s='foobar'

print(s[::-1] [::-1]is s)