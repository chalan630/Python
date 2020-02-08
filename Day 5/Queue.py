'''
@Description: 线程优先级队列
@Author: chalan630
@Date: 2019-12-29 00:43:28
@LastEditTime : 2019-12-29 01:07:49
'''
'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，
和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，
可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.get(block=True, timeout=None)从队列中移除并返回一个项目。
    Queue.put(item, block=True, timeout=None)将 item 放入队列。
'''

from queue import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
for word in nameList:
    workQueue.put(word)

# 等待队列空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
