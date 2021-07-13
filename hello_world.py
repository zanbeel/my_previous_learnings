

def say_hello(name):
    print(f'Hello {name}')

say_hello("abc")

print()

def say_hello(*args):
    print('hello world',args)
say_hello('xyz','cdf','ghk')