import os


def split_file(filename):
    with open(filename, 'r') as input_file :
        lines = [line.rstrip('\n') for line in input_file]
        for idx, line in enumerate(lines):
            with open('output_{0}.txt'.format(idx), 'w') as output_file:
                output_file.write(line)

    print('Well done !')


# split_file(os.path.join(os.getcwd() ,'mytest.txt'))
split_file('mytest.txt')