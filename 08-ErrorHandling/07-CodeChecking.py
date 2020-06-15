# dictionary.get(keyname, value)
# method returns the value of the item with the specified key.


def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)


if __name__ == '__main__':
    #print(f('a'))
    #print(f('b'))
    #
     print(f('c'))  # if key not exists returns 9
     print(f(6666))
