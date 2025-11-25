def reverse_words(sentence):
    list_of_words=sentence.split()
    reverse_list=[]
    for word in list_of_words:
        reverse_list.append(word[::-1])
    s=" ".join(reverse_list)
    result=''
    counter=0
    for c in sentence:
        if c== " ":
            result+=' '
        else:
            result+=s[counter]
            counter+=1
            
    

    return result

print(reverse_words("Hello World"))
print(reverse_words("Python is fun!"))
print(reverse_words("This is a  test   with   multiple spaces"))
print(reverse_words("s'teL    ecitcarp"))
print(reverse_words("Diyorbek"))
print(reverse_words("Humoyun"))

# olleH dlroW
# nohtyP si !nuf
# sihT si a  tset   htiw   elpitlum secaps
# Let's    practice