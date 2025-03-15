# list comprenhnsion
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

print(f"{[i*i for i in range(10)]}")
print(f"{[i*i for i in range(10) if i % 2 == 0]}")
print(f"{[i*i if i % 2 == 0 else 0 for i in range(10)]}")

#dicttonary compreshncion

print(f"{ {x:x*x for x in range (10)} }")

#set co
#print(f"{ (x*x for x in range(10)) }")

# function args and keywordargs
def arithmetic(x,y):
    z = x + y
    return z
print(arithmetic(25,7))

# args

def arithm(*args):
    print(f"Type of args {type(args)}")
    add = 0
    for x in args:
        add += x
    return add

print(arithm(4,5,6,7))
#kw args

def my_func(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, value)
    
print(my_func(name="sharath",age = 30))
        