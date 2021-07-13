number=7
print(input("enter any number from 1 to 10 "))
guess=int(input())

if guess==number:
    print("congratulations: right answer")
    print("please guess lower")

elif guess<number:
    print("please guess higher")

else:
    print("try again")