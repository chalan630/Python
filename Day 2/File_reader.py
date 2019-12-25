import os

path = os.path.dirname(__file__)
with open(path + '/pi_digits.txt', 'r') as file_object:
    contents = file_object.read()                           # 整体读取
    print(contents.rstrip())
    for line in file_object.readlines():                    # 逐行读取
        if line == '\n':
            pass
        else:
            print(''.join(line.strip()))
