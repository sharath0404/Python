import re

words = "HI sharath practive well the regex its imp topic Apr 4th"

a = "good day"
print(f"addtess {id(a)}")
a = a.replace("day","today")
print(f" address {id(a)}")

# search find only first occurence in the sentence
# if not fount it will return none
#() -> used to capture groups.
#[] -> capture a sequence of characters.
match = re.search(r'imp',words)
regex_match = r'[a-zA-Z]+ (\d+)'
new_match = re.search(regex_match, words)
if new_match != None:
    print(f"New match at index {new_match.start()} and end {new_match.end()}")
    print(f"")
print(f"the new match {new_match}")
print(f"start_index is {match.start()}")
print(f"End index is {match.end()}")

#findall it finds all matching occurance in list

new_words = """
                Hi my name is sharath my num is 1234
                My friend num is 3001 and his num 2342 
                """
regex = r'\d+' # one or more digit
regex1 = r'[A-Z][a-z]+'
match = re.findall(regex,new_words)
print(match)

# re.compile in python is used to compile a regular expression pattern
#into a regex object which can be used for matchin searchin efficiently

pattern = re.compile(r'\d+')
s = """
    Hi my name is sharath my num is 1234
    My friend num is 3001 and his num 2342 
    """
match = pattern.findall(s)
print(match)
# validate email
email_patr = r'[a-zA-Z0-9._%+]@[a-zA-Z0-9.-_].[a-zA-Z]{2,}'

# re.split and str.split the key difference is re.split works on multiple delimters
#str.split works on only one delimeter
# - indicates range of characters use carefully inside[...]
fruits = "apple; mango, banana-orange"
words = re.split(r'[\s;,-]+',fruits)
print(words)

# re.sub used to substitute 
# re,sub(pattrern,replace_str,String,count=3,flags=re.IGNORECASE)

words = "hey man you man am man you junk man"
subs = re.sub("man","**",words,count=2)
print(subs)
# subn similar to sub the main diff is subn provies tuple count how much it reolaces
words = "hey man you man am man you junk man"
print(re.subn("man","$$",words))
t = re.subn("man","$$",words)
print(t)
print(len(t))
print(t[0])

# re.escape ensures special characters are treated as normal text

text = "Price is $5.99 per item."
pattern = re.escape("$5.99")  # Escaping special characters

match = re.search(pattern, text)

print(f"Pattern: {pattern}")
print(f"Match found: {match.group() if match else 'No match'}")
