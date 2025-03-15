#def hello():
 #   print("Hello sharath")

#def world():
#    print("Hi sharath")
    
#x = hello(world)
#x()

# def hello(x):
#     x()
#     print("Hello India")
    
# def world():
#     print("Hello world")

# hello(world)
# def hello():
#     def wrapper():
#         print("AM inside wrapper")
#     wrapper()
    
# hello()

# def hello():
#     def wrapper():
#         print("From wrapper")
#     return wrapper

# x = hello()
# x()


    
# import time
# def timedecorater(func):
#     def wrapper():
#         start = time.time()
#         print("Am calling inside wrapper")
#         func()
#         time.sleep(5)
#         print("Time taken to execujte ", time.time() - start)
#     return wrapper

# #x = timedecorater(display)
# #x()
# @timedecorater
# def display():
#     print("Am printing display function")
        
# display()

# with args and key args 
# import time
# def timedecorater(func):
#     def wrapper(*args,**key_args):
#         start = time.time()
#         func(*args,**key_args)
#         print(f" Time take n to execu is {time.time() - start}")
#     return wrapper

# @timedecorater
# def display(name,age):
#     print(f" Hey my name is {name} and my age is {age}")

# @timedecorater
# def test(**keyargs):
#     print(f"Am prtinting type {type(keyargs)} with values {keyargs}")
    
# display("sharath",30)
# test(quality="good",price=2000)

def log_decorater(func):
    def wrapper(*args,**key_args):
        print(f"This is what i received for func {args},{func.__name__}")
        ret = func(*args,**key_args)
        print(f"This is what i received {ret}")
    return wrapper

@log_decorater
def display(name,age):
    print(f" Hey my name is {name} and my age is {age}")
    
display("sharath",30)

























