def checkParentheses(mystring):
    count = 0
    for i in mystring:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        # if count < 0:
        #     return False
    return count == 0


print(checkParentheses('(2+(3+4))'))  # returns True
print(checkParentheses('(2+(3+(4)'))  # returns False
