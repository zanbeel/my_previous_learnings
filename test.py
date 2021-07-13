lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
start = 11
end = 25
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)

n=int(input())
for i in range(1,int(n)):
    for j in range(2,(i+1)):
        if i%j==0:
            if i==j:
                print(i)
            break
# does not produce correct result:
x = 8
for num in range(x):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)