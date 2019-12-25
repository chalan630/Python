filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("oh, my son!\n")                  # 写入文件
    file_object.write("oh, my dog son!\n")              # 写入多行

with open(filename, 'a') as file_object:
    file_object.write("oh, my son!\n")                  # 追加文件
    file_object.write("oh, my dog son!\n")              # 追加多行
