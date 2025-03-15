#condition

a = 10
b = 20

if a > b:
    print(f" the value {a} is greater")
elif b > a:
    print(f"The value {b} is greater")
else:
    print("They are equal")
    
# while loop

x = 0
while x < 10:
    print(x)
    x = x + 1

for i in range(10):
    print (i)
    
# data structures
my_temp = [1,2,3]
my_dict = {'a' : 10,
            'b': 20,
           "name": "sharath",
            "my_list": my_temp
            }
print(my_dict['my_list'])

my_set = set() # to intialize set dont use {} its treated as dic