def are_anagrams(string1, string2):
    string1=string1.strip().lower().replace(' ', '').replace('.', '')
    string2=string2.strip().lower().replace(' ', '').replace('.', '')
    new_list1=list(string1)
    new_list2=list(string2)
    new_list1.sort()
    new_list2.sort()
    s1="".join(new_list1)
    s2="".join(new_list2)
    print(s1)
    print(s2)
    if s1==s2:
        return True
    else:
        return False




    # len()
    # for c in string1:
    #     if not c in string2:
    #         return False
    #     else:
    #         return True
        
print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))