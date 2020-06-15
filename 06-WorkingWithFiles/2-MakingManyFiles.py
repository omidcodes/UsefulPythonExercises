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
make_many_files(r"H:\MAPSAExercises\mygitlab\PythonMapsa\pythonmapsa\ClassExercises\06-WorkingWithFiles\testfolder" , 20)

# make_many_files("H:\\m", 4)
