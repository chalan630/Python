users = ['andrew', 'carolina', 'david']
user = 'marie'

# 检查特定值是否包含在列表之中
if user in users:
    print(user)

# 检查特定值是否不包含在列表之中
if user not in users:
    print(user)

# if--else
if user not in users:
    users.append(user)
else:
    print("User already exists")

# if--elif--else
if user not in users:
    users.append(user)
elif user == 'root':
    print("welcome!")
else:
    print("User already exists")
