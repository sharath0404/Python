#slicing in list

my_list = [1,2,"sharath",5,4,2,4]

print(my_list)

print(my_list[3:8:1])# by default start = 0(inclusive) stop = len() exclusive step = 1

print(my_list[8:2:-1]) # start > stop in reverse index

# nested value how to print

my_list = [1,3,6,3,[4,4,4],9]

for i in my_list:
    if isinstance(i,list):
        for y in i:
            print(f"Inner looop {y}")
    else:
        print(f"outer {i}")
        
# tuple
my_tup = ()
#print(dir(my_tup))
#print(dir(my_list))
my_tup = (1,4,5,6,6,4,4)
print(my_tup.count(4))
print(my_tup.index(4))

#string
#string is immutable

# dictonary
my_dict = {}

my_dict = {'a': 100, (1,2,3):555, 1:(4,5,6)}
for x in my_dict.keys():
    print(x)
for x in my_dict.values():
    print(x)

for key,values in my_dict.items():
    print(f"Printing both keys {key} and values{values}")