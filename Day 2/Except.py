# 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("Error!")

# 使用异常处理避免崩溃
try:
    """可能出现异常的代码块"""
    pass
except BaseException:
    """发生异常后的做法"""
    pass
else:
    """异常代码正常执行时运行的代码"""
    pass
