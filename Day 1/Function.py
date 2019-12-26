'''
@Descripttion: 函数操作
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime : 2019-12-26 11:42:13
'''
# 传递实参
# 如果函数定义中未使用 / 和 *，则参数可以按位置或按关键字传递给函数

# 位置实参
def describe_pet(animal_type, pet_name):                        # 定义时可以使用默认值
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')                                # 位置实参
describe_pet(animal_type = 'hamster', pet_name = 'harry')       # 关键字实参

# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name = ''):        # middle_name 为可选实参
    """显示宠物信息"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name

# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


# 传递列表
def greet_users(names):
    """传入列表"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

# 禁止函数修改列表
def greet_users(names[:]):
    """传入列表"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

# 传递任意数量的实参
def make_pizza(*toppings):                # 将传入参数装入元组
    """输出任意长度的参数"""
    print(toppings)

# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):                # 将传入参数装入元组
    """输出任意长度的参数"""
    print("\nMaking a " + str(size) + "pizza.\n" + toppings)

make_pizza(12, 'mushrooms', 'green peppers')
make_pizza(10, 'mushrooms')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):    # 将参数加入字典
    """创建一个字典类，其中包含我们知道的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items()
        profile[key] = value
    return profile

build_profile('albert', 'einstein', location = 'princeton', field = 'physics')


