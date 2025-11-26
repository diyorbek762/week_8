def decompress_rle(encoded_string):
    letter=''
    number=''
    result=[]
    for i in range(0, len(encoded_string)):
        if encoded_string[i] in '1234567890':
            number=number+encoded_string[i]
        elif not encoded_string[i] in '1234567890':
            letter=letter+encoded_string[i]
            result.append(int(number)*letter)
            letter=''
            number=''

    return "".join(result)




    






    
print(decompress_rle("3A2B4C"))
print(decompress_rle("1W4B1W"))
print(decompress_rle("10X1Y"))
print(decompress_rle("1A1B1C1D1E"))
print(decompress_rle("12Z"))










    # for i in range(0, len(encoded_string), 2):
    #     new_list.append(int(encoded_string[i])*encoded_string[i+1])
    # return "".join(new_list)



# new_list_numbers=[]
    # counter=0
    # for j in range(0, len(encoded_string)):
    #     if not 'a' <= encoded_string[j] <= 'z':
    #         counter+=1
    #         if len(new_list_numbers)==0:
    #            new_list_numbers.append(encoded_string[j:counter])
    #         else:
    #            new_list_numbers[0]=new_list_numbers[0]+encoded_string[j]
    #     else:
    #         continue

    # return new_list_numbers

