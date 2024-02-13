import zipfile

# Replace it with anything you want
PATH = "myUnzippedFolder"

def read_zipfile(zipfilename):
    with zipfile.ZipFile(zipfilename) as myzip:
        # ExtractingFiles
        myzip.extractall(path=PATH)
        print('file successfully unzipped')

        # Reading Some files from zip file without need to extracting
        with myzip.open('mytestfile.txt', 'r') as myfile:
            print(str(myfile.readlines()))


read_zipfile('mytest.zip')
