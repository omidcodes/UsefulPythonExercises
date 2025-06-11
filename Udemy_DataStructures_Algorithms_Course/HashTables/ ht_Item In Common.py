

def item_in_common(list1, list2)-> bool:

    dict1 = {}

    for item in list1:
        dict1[item] = True
    
    for item in list2:
        if item in dict1.keys():
            return True
        
    return False




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""