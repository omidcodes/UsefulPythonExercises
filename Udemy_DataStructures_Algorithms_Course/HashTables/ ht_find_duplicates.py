def find_duplicates(list):
    occurance_dict = {}

    for item in list:

        if item in occurance_dict:
            occurance_dict[item] += 1
        else:
            occurance_dict[item] = 1

    duplicate_items = []

    for key in occurance_dict:
        if occurance_dict[key] >1:
            duplicate_items.append(key)
    return duplicate_items


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

