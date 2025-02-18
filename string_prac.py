# only first world is capitalized 
# all other string remains same
text = "hello World"
capatized_text = text.capitalize()
print(f"Capitalized string is {capatized_text}")

# To convert text to lower
text = "HELLo World"
lower_case = text.lower()
print(f"Lower case of '{text}' is '{lower_case}'")

#To convert text to upper
text = "Hello World"
upper_case = text.upper()
print(f"the upper case of '{text}' is {upper_case}")

# To count number of characters in string
text = "Hello Sharath How are you"
count_char = text.count('H')
print(f"The total number of H char in '{text}' is {count_char}")

from collections import Counter
# to count insensitive data
text = "Hello Sharath How are you"
count_ins_counter = Counter(text)
#print(f" The insensitive data is {count_ins_counter} ")

# check the string starts with particular world or not
text = "Hi Sharath how are you"
start_string = text.startswith("Hi")
print(f"The String '{text}' starts with {start_string}")

# check the string ends with particular world or not
text = "Hey hello"
end_string = text.endswith("hello")
print((
      f"String ends with {end_string} and type"
      f" of end_string is {type(end_string)}"))
# find is used to check substring in a string it return index
# syntax .find(substring,start,end) here start and end optional

text = "Hi sharath work hard work"
sub_str_find = text.find("work")
print(f"index position of substring is {sub_str_find}")
#last occurence
sub_str_find = text.rfind("work")
print(f"index position of last occurence is {sub_str_find}")

#index both index and find returns index of the word or character the main difference
#is index return erro if not handled properlt program may crash whereas
# ind return -1 if substring not found
text = "Hello man the man index man"
try:
    index_sub = text.index("python")
except ValueError:
    print(f" the substring not found")

#format
name = "Sharath"
age = 30
message = "Hi i am {} and am {} years old".format(name,age)
print(message)

#isalnum() it allows only alphabets or num doesn't allow any special character
# only letter or only numbers also fine
text = "sharath124"
check_alpanum = text.isalnum()
print(f"The alpha numeric is {check_alpanum}")

# only alphabets
name = "Onlyalphabet"
only_alpha= name.isalpha()
print(f"wheather only alphabet is present {only_alpha}")

# decimals allows only 0-9
text = '1234'
text1 = "1\u20823"
only_decimals = text.isdecimal()
print(f"only decimals is there {only_decimals} and {text1.isdecimal()}")

# digit allows decimal + subscripts
text = "1\u20823"
deci_sub_sup = text.isdigit()
print(f"allows {text} sub and superscripts {deci_sub_sup}")

# numeric allows digit + fraction all numeric value
text = "1\u20442"
cleaned_text = text.replace("\u2044", "") 
num_all = cleaned_text.isnumeric()
print(f"the {cleaned_text} num_al is {num_all}")

#is lower 
text = "hello"
check_lower = text.islower()
print(f"Checj the string is lower {check_lower}")

#is upper
text = "HELLO"
check_upper = text.isupper()
print(f"Check if its upper {check_upper}")

# join command seperator.join(iterable)
# iterable -> A list tuple or any iterable containing strings

words = ["Hello", "sharath", "python"]
joinable_text = "-".join(words)
print(f" the joinable text is {joinable_text}")

# replace string.replace(old,new,count) count is optional
# here count specify that number of occurences you want to replace
# by default all the occurence will replace
words = "hello world man world"
rep_string = words.replace("world","python",1)
print(f" the replaced string is {rep_string}")

# maketrans() and translate() in python both are used to
#replace or remove characters in string efficiently
# str.maketrans(old_chars,new_chars,remove_chars(optional))
#Length of old and new chars should be same

words = "!!! Hi sharath !!!"
new_table = words.maketrans("ah","ie","!")
new_str = words.translate(new_table)
print(f" the new string is {new_str}")

#strip in python removes leading and trailing whitespace
#or charactes from a string default it remove spaces
# string.strip(chars)

words = "           00hello world00     "
strip_text = words.strip(" 0")
print(f"the {strip_text}") 

#The split methods breaks a string into list of substrings based on specified delimeter
# string.split(seperator,MAxsplit) here both are optional and we by default " " is seperator


words = "hi hello how"
new_word = words.split()
print(f"the new word is {new_word} {new_word[-1]}")

# partition is a method splits a string into three parts based in the first occurence
#of a specified seperator

name = "Hello world sharath"
part_name = name.partition(" ")
print(f" the part name is {part_name}")
#pallindrome
name = "MADAM"
print(f" {name} and {name[0::-1]}")

# splitlines() is amethod splts a string into a list based on line breaks
#\n \r or \r\n key diff b/w this and split(\n) split wont handle \r\n (windows)

name = "hello\n\nsharath\r\nman"
lines_split = name.splitlines()
print(f"the splitliness is {lines_split}")

# zfill method pads a zero at the begining until it reaches specified length
#string.zfill(width)
#width->total length after adding leading 0
name = "45"
new_text = name.zfill(5)
print(f" the new o/p is {new_text}")

#encode converts strings to bytes using specified encoding format

text = "hello"
encoded_text = text.encode()
print(f"the encided striing is {encoded_text}")

#removeprefix
text = "sharath_the_great"
pre = text.removeprefix("sharath_")
print(f" the suffix removed is {pre}")

#removesuffic
text = "god_is_great am god"
suf = text.removesuffix("god")
print(f" the suf is {suf}")

#slicing
#sequence[start:stop:step]
#start -> default 0 included
#stop -> the ending index excluded
#step -> how many elements to skip 1
#list slicing also possible

text = "ABCDEFGH"
print(f"the text val is {text[5::-1]}")