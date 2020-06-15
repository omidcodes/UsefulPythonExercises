def count_lines_characters(filename='mytest.txt'):
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        num_lines = len(lines)
        num_characters = 0
        x = lambda lines: sum(len(line) for line in lines)
        num_characters = x(lines)
        print("Total lines: {}".format(num_lines))
        print("Total Characters: {}".format(num_characters))




count_lines_characters('mytest.txt')
