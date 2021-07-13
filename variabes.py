m = 700
k = 700
print(id(m))
print(id(k))

m = 'this'
k = m
print(id(m))
print(id(k))

m = 'this'
k = 'this'
print(id(m))
print(id(k))

m = 300
k = 300
print(id(m))
print(id(k))

Deep Dive: Caching Small Integer Values

From what you now know about variable assignment 
and object references in Python, the following probably won’t surprise you:

>>> m = 300
>>> n = 300
>>> id(m)
60062304
>>> id(n)
60062896
With the statement m = 300, Python creates an integer object with
 the value 300 and sets m as a reference to it.
  n is then similarly assigned to an integer object with 
  value 300—but not the same object. Thus, they have different
 identities, which you can verify from the values returned by id().

But consider this:

>>> m = 30
>>> n = 30
>>> id(m)
1405569120
>>> id(n)
1405569120
Here, m and n are separately assigned to integer objects having value 30. 
But in this case, id(m) and id(n) are identical!

For purposes of optimization, the interpreter creates objects 
for the integers in the range [-5, 256] at startup, 
and then reuses them during program execution. Thus, when you assign 
separate variables to an integer value in this range,
 they will actually reference the same object.