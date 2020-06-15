'''
palindrome Strings :
The characters read the same backward as forward. Some examples of palindromic words are
redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, madam, and refer
'''


def findPalindromeStrings(mystring):
    if mystring == ''.join(reversed(mystring)):
        return True
    else:
        return False


print(findPalindromeStrings('radar'))
print(findPalindromeStrings('omid'))
print(findPalindromeStrings('level'))
