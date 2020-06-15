# Lambda 1
myfunc = lambda x : x*2
print(myfunc(4))

#Lambda2
a = [(3,4), (7,1), (5,9), (2,2)]
a.sort(key=lambda x: x[1])
print(a)


# map + lambda
numbers = [10,11,8,6,100,7,9,21]
myfunc = lambda x: 'small' if x<10 else 'big'
answer = list(map(myfunc , numbers))
print(numbers)
print(answer)


# map + lambda + filter
my_list = [1,5,6,8,10,11]
myfunc2 = lambda x: x%2==0
f = filter(myfunc2, my_list)
print(list(f))
