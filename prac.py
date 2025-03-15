data = ['A','B','C','d']
print(f"""address os data = {id(data)} and A address = {id(data[0])} 
      B address = {id(data[1])}""")
data2 = "Sharath"
data3 = data2
print(f"""data2 add = {id(data2)} and data2[0] = {id(data2[0])}
      and {id(data2[1])} and add of data3 = {id(data3)}""")


data = [1,2,3,4]
#data.extend([1,2,3])
#print(f"data = {data}")

data.pop(2) # pop will work on index
print(f"poped data = {data}")
data.remove(4) # it will work on particular num
print(f"remove data = {data}")
data.clear()#remove all the element
print(f"poped data = {data}")

#del data 
#print(data)
data = "India"
#del data
list_data = list(data)
print(f" split {list_data}")
# convert back into array we can use join method
print(f" Join = {'--->'.join(list_data)}")



data = ['A', 'B', 'C','D','E']

data.insert(len(data),20)
print(f"data = {data}")
# List [] and tuple () here the data is immutable {} set
# tuple is faster and its constant, so if you want to save time will go for tuple
# tuple cannot be modified (CRUD not allowed)

data = ('A','B','C')

# it can be modified only one way
data1 = [1,2,3]
data2 = ('i','N','D',data1)
print(data2)
data1.append(100)
print(data2)

print(data2.count('i'))

# set will remove duplicate and its unorders means i cant acces
# using index 
# - operator only work on set 

data1 = {1,2,3,1,4,6,1,9,9}
print(data1)

# Dictoranries key value pair
Names = {
    "sharath":"gowda",
    "sneha":"wife",
    "krishna":"daughter",
    "MyLove":"Krishna"
}
print(f"{Names.get("sharath")}")
my_list = list("it defined")
print(my_list)
my_list = [] * 5
print(my_list)

def func(name,state="karnataka",district="dds"):
      print(f"Am {name} and am from {district}, {state}")
      
func("sharath",district="Hassan",state="Karnataka")