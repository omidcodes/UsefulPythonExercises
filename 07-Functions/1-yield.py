def read_file(path, block_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default block size: 1k."""
    with open(path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield data


# running Generator (with Lazy function)
x = read_file('mytest.txt')
# print(x.__iter__().__next__())
for piece in x:
    print(piece)
