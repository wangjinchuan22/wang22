import threading
import time


def work(name):
    print(name + "开始工作")
    time.sleep(3)
    print(name + "工作结束")

def eat(name):
    print(name + "开始吃饭")
    time.sleep(2)
    print(name + "吃饭结束")

if __name__ == "__main__":
    thread_s = []
    t1 = threading.Thread(target=work,args=(("wjc",)))
    t2 = threading.Thread(target=eat,args=(("wjc",)))
    thread_s.append(t1)
    thread_s.append(t2)
    for t in thread_s:
        t.start()
    for i in thread_s:
        i.join()