# available_exits= ['norh', 'south' , 'east' , 'west']

# chosen_exit = ""
# while chosen_exit not in available_exits:
#         chosen_exit = input("please choose a direction: ")

# print("aren't you glad you got out of there")

## to end this loop we can use break

available_exits= ['norh', 'south' , 'east' , 'west']

chosen_exit = ""
while chosen_exit not in available_exits:
        chosen_exit = input("please choose a direction: ")
        if chosen_exit.casefold()=="quit":
            ##casefold is used to make quit not case sensitive
            print("Game over")
            break

##print("aren't you glad you got out of there")

## to get rid of last line arent you glad... we will do it this way

