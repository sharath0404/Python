def find_nth_occurence(text,word,n):
    start = 0
    count = 0
    while True:
        index = text.find(word,start)
        if index == -1:
            print(f"The given substring not exists ")
            return -1;
        count = count + 1
        if n == count:
            return index
        start = index + 1

text = input("Enter the text: ")
word = input("Enter the substring to search: ")
nth_occurence = int(input("Enter the occurence you want to enter: "))

index = find_nth_occurence(text,word,nth_occurence)

if index != -1:
    print(f"The substring {word} find at the {index}")
else:
    print(f"The substring {word} is not found")
        
        
    
