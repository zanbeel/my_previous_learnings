# parrot = "Norwegian Blue"

# letter = input("Enter a character: ")

# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't need that letter")


# number = "9,223;372:036 854,775;807"
# separators = ""

# for char in number:
#     if not char.isnumeric():
#         separators = separators + char

# print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

number = input('please enter a series of numbers, using any separators you like:')
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

capital = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for uppercase() in capital: