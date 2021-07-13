"""

first_name='Eric'
message=f"Hello, {first_name} would you like to learn some python today?"
print(message)

first_name='imran'
last_name='khan'
message=f'Hello, {first_name.title()} {last_name.title()} would you like to learn some python today?'
print(message)


title='Mr. President'
message=f"Hello {title.lower()} today's first meeting is 10'0 clock today"
print(message) 

Celebration='moon sighting'
message= f'After {Celebration.upper()} all Muslims celebrate Eid'
print(message) """

quote='Eintstein said,'
message=f'{quote}"Two things are infinite, the universe and human stupidity,\n and I am not sure about the universe."'
print(message)

famous_person='Einstein'
message=f'{famous_person}" said Two things are infinite, the universe and human stupidity,\n and I am not sure about the universe."'
print(message)


name=' Einstein '
message=f'{name.lstrip()}"said Two things are infinite\t\n the universe and human stupidity\n and I am not sure about the universe."'
print(message)

print()

name=' albert '
message=f'{name.rstrip()}"said Two things are infinite\t\n the universe and human stupidity\n and I am not sure about the universe."'
print(message)

print()

name=' Who '
message=f'{name.strip()}"said Two things are infinite\t\n the universe and human stupidity\n and I am not sure about the universe."'
print(message)

print(4+4)

print(4*2)

print(16/2)

print(2**3)

number=7
print(f'{number} is my favourite number')

friends_list=['nadeem', 'waseem', 'raheem', 'shameem', 'kareem']

print(f'how are you {friends_list [0],[1],[2]}*args,')