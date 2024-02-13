# len
# max
# sum
# min
# in
# reversed


# len
def findLen(string):
    count = 0
    for i in string:  # Counting character in a string
        count += 1
    return count  # Returning count


# max
def findMax(mylist):
    max = mylist[0]
    for item in mylist:
        if item > max:
            max = item
    return max


# sum
def findSum(*args):
    if len(args) <= 0:
        return None
    else:
        mysum = 0
        for num in args:
            mysum += float(num)
    return mysum


# min
def findMin(mylist):
    min = mylist[0]
    for item in mylist:
        if item < min:
            min = item
    return min


# in
def findIn(mylist):
    l = len(mylist)
    counter = 0
    if l <= 0:
        return None
    else:
        while counter < l:
            print(mylist[counter], end=' ')  # Write Anything you want to Do here
            counter += 1
    return None


# reversed
def findReversed(mylist):
    return mylist[::-1]


if __name__ == '__main__':
    string = "OmidHashemzadeh"
    mylist = [4, 19, 2, 11, 166, 14]

    print(findLen(string))

    print(findMax(mylist))

    print(findSum(4, 5, 6))

    print(findMin(mylist))

    findIn(mylist); print('\n')

    print(findReversed(mylist))
