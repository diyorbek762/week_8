def are_anagrams(string1, string2):
    string1= string1.strip().lower()
    string2=string2.strip().lower()
    for c in string1:
        if not c in string2:
            return False
        else:
            return True
        
print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))