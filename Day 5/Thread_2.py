'''
@Descripttion: 继承式调用多线程
@Author: chalan630
@Date: 2019-12-28 21:06:50
@LastEditTime : 2019-12-31 10:05:04
'''

import threading
import time

'''
threading.currentThread()       # 返回当前的线程变量
threading.enumerate()           # 返回一个包含正在运行的线程的list
threading.activeCount()         # 返回正在运行的线程数量
run()                           # 用以表示线程活动的方法
start()                         # 启动线程活动
join([time])                    # 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
isAlive()                       # 返回线程是否活动的
getName()                       # 返回线程名
setName()                       # 设置线程名
'''

exitFlag = 0

class myThread(threading.Thread):                   # 直接从 threading.Thread 继承创建一个新的子类
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)             # super(myThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
    
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
