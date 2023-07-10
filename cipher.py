# Author: Juba Twain.
text = input("Give me text: ") #normal text
key = int(input("Key: ")) 
output = ""
for char in text: #for each character in the text entered,
    #we're gonna add it to the output string
    output += chr(ord(char) ^ key) #ord finds the scode. chr turns scode back to character
print(output)
