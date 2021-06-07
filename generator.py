import hashlib


def hash_file(filepath):
    try:
        with open(filepath, 'r') as datafile:
            for line in datafile.readlines():
                yield hashlib.md5(line.encode('utf-8')).hexdigest()
    except FileNotFoundError as error:
        print(error)