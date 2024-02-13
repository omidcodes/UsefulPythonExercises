import zipfile


def bruteforce(filename, dictionary):
    password = None
    file_to_open = zipfile.ZipFile(filename, 'r')
    with open(dictionary, 'rb') as f:
        for line in f.readlines():
            password = line.strip()
            try:
                file_to_open.extractall(pwd=password)
                print(f'Password found: {password}')
                break
            except Exception as e:
                # print(str(e))
                pass


if __name__ == '__main__':
    filename = 'mytestzip.zip'
    dictionary = 'mypasswordlist.txt'
    bruteforce(filename, dictionary)
