# calling format: ex : make_many_files("H:\\m", 4)
import os

os.path.join('')
def make_many_files(path, n):
    os.chdir(path)
    for i in range(n):
        with open('file{0}.txt'.format(str(i)), 'w+') as f:
            f.writelines('Hello. I,m virus !')
    print('Well Done!')

# you can replace address with %appdata%
path = r"/tmp/testfolder/"
make_many_files(path , 20)

# make_many_files("H:\\m", 4)
