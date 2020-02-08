'''
@Description: 线程同步
@Author: chalan630
@Date: 2019-12-29 00:31:01
@LastEditTime : 2020-02-08 15:24:02
'''
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()
    
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

'''Lock
实现原始锁对象的类。一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，
直到它被释放；任何线程都可以释放它。
acquire(blocking=True, timeout=-1) 可以阻塞或非阻塞地获得锁。
release()释放一个锁。这个方法可以在任何线程中调用，不单指获得锁的线程。
'''

'''RLock
此类实现了重入锁对象。重入锁必须由获取它的线程释放。一旦线程获得了重入锁，
同一个线程再次获取它将不阻塞；线程必须在每次获取它时释放一次。
acquire(blocking=True, timeout=-1)可以阻塞或非阻塞地获得锁。
        当无参数调用时： 如果这个线程已经拥有锁，递归级别增加一，
        并立即返回。否则，如果其他线程拥有该锁，则阻塞至该锁解锁。
release()释放锁，自减递归等级。如果减到零，则将锁重置为非锁定状态，
        并且，如果其他线程正被阻塞着等待锁被解锁，则仅允许其中一个线程继续。
        如果自减后，递归等级仍然不是零，则锁保持锁定，仍由调用线程拥有。
'''

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

