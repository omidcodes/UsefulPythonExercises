import string
import random


def randompassword(length):
    complexity = int(input('Please Choose complexity (1:simple, 2:medium, 3:complex):  '))

    if complexity == 1:
        chars = string.digits
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
    elif complexity == 3:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print('Wrong input.');
        return None
    # size = random.randint(length, length)
    return ''.join(random.choice(chars) for x in range(length))

if __name__ == '__main__':
    print(randompassword(10))