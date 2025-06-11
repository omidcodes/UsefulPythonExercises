def first_non_repeating_char(text:str):
    
    dict1 = {}

    for idx, char in enumerate(text):
        if char in dict1.keys():
            dict1[char][0] += 1
        else:
            # (number_of_occurance, first_occurance_position). e.g: [3, 2]
            dict1[char] = [1 , idx]
    
    min_first_occurance_position = 10 ** 10
    output = None

    for key, val in dict1.items():

        number_of_occurance, first_occurance_position = val

        if number_of_occurance == 1 and first_occurance_position < min_first_occurance_position:
            min_first_occurance_position = first_occurance_position
            output = key
            
    return output


print(first_non_repeating_char('leetcode') )

print(first_non_repeating_char('hello') )

print(first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""