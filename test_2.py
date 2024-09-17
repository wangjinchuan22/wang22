import threading
import time
import queue
#------------------------------多线程------------------------------------------------
# def work(name):
#     print(name + "开始工作")
#     time.sleep(3)
#     print(name + "工作结束")
#
# def eat(name):
#     print(name + "开始吃饭")
#     time.sleep(2)
#     print(name + "吃饭结束")
#
# if __name__ == "__main__":
#     thread_s = []
#     t1 = threading.Thread(target=work,args=(("wjc",)))
#     t2 = threading.Thread(target=eat,args=(("wjc",)))
#     thread_s.append(t1)
#     thread_s.append(t2)
#     for t in thread_s:
#         t.start()
#     for i in thread_s:
#         i.join()

##--------------------------多线程使用队列-----------------------------------------
# def producer(q):
#     for i in range(5):
#         q.put(i)
#         print("队列进入数据：" + str(i))
# def consumer(q):
#     while not q.empty():
#         item = q.get()
#         print("consumed:",item)
#         # time.sleep(1)
# if __name__ == "__main__":
#     q = queue.Queue()
#     producer_t = threading.Thread(target=producer,args=(q,))
#     consumer_t = threading.Thread(target=consumer,args=(q,))
#     producer_t.start()
#     consumer_t.start()
#     producer_t.join()
#     consumer_t.join()


##------------------------------线程锁使用-----------------------------------------------------
lock = threading.Lock()

import os,time
def work():
    global n
    with lock:
        temp = n
        time.sleep(0.1)
        n = temp - 1
        print(n)
    ###  没  有   加  锁
    # temp = n
    # time.sleep(0.1)
    # n = temp - 1
    # print(n)
if __name__ == "__main__":
    n = 100
    l = []
    for i in range(100):
        p = threading.Thread(target=work)
        l.append(p)
        p.start()
    for j in l:
        j.join()
    print(n)