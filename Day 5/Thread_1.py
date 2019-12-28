'''
@Descripttion: 
@Author: chalan630
@Date: 2019-12-29 01:10:41
@LastEditTime : 2019-12-29 01:16:22
'''
import time
import threading

def song(a,b,c):
    print(a, b, c)
    for i in range(5):
        i = i
        print("song")
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=song,args=(1,2,3)).start()
    threading.Thread(target=song,kwargs={"a":1,"c":3,"b":2}).start()        # 参数顺序可以变
    threading.Thread(target=song,args=(1,),kwargs={"c":3,"b":2}).start()    # 混合使用元组和字典
