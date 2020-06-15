def func(mystr):
    x = mystr.split(" ")
    return (x[1],x[0])

# TEST
print(func("hello world"))