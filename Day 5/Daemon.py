'''
@Descripttion: 守护线程
@Author: chalan630
@Date: 2019-12-31 10:05:19
@LastEditTime : 2020-01-05 12:59:51
'''
import threading
import time

'''
主线程启动子线程前把子线程设置为守护线程。
只要主线程执行完毕，不管子线程是否执行完毕，就结束。
但是会等待非守护线程执行完毕
主线程退出，守护线程全部强制退出。
'''

def run(n):
    print("task",n)
    time.sleep(2)
    print("task has done!")     
start_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)  #把当前线程设置为守护线程，一定在start前设置
    t.start()
print(threading.current_thread(),threading.active_count())
print(time.time()-start_time)  