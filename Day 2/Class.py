# 创建类
class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")
    
    def update_age(self):
        self.age += 1

my_dog = Dog('willie', 6)           # 实例化
my_dog.name                         # 访问属性
my_dog.sit()                        # 调用方法
# 修改属性的值
my_dog.age = 7                      # 直接修改属性值
my_dog.update_age()                 # 通过方法修改属性值

