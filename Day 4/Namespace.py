'''
@Descripttion: 变量的作用域
@Author: chalan630
@Date: 2019-12-27 10:28:39
@LastEditTime : 2019-12-28 20:49:33
'''
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 命名空间查找顺序：
# 局部>全局>内置

var1 = 5                    # var1 是全局名称
def some_func():
    var2 = 6                # var2 是局部名称
    global var1             # 内部作用域想修改外部作用域变量
    var1 = 51
    print(var1)
    # output:51
    def some_inner_func():
        var3 = 7            # var3 是内嵌局部名称
        nonlocal var2       # 修改嵌套作用域而非全局作用域
        var2 = 61
        print(var2)
        print(var3)
        # output:61
        # output:7
    some_inner_func()
    print(var2)
    # output:61

some_func()
print(var1)
# output:51
