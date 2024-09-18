# import multiprocessing
# import time
# def eat(name):
#     print(name + "开始吃饭")
#     time.sleep(2)
#     print(name + "吃饭结束")
#
# def work(name):
#     print(name + "开始工作")
#     time.sleep(2)
#     print(name + "工作结束")
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=eat,args=("wjc",))
#     p2 = multiprocessing.Process(target=work,args=("wjc",))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


from multiprocessing import Pool,Process
import time

def Foo(i):
    time.sleep(2)
    return i + 100
def Bar(arg):
    print(arg)

if __name__ == "__main__":
    p_start = time.time()
    pool =Pool(5)           ##进程池，
    for i in range(5):
        # pool.apply_async(func=Foo,args=(i,),callback=Bar,error_callback=None)  ##非阻塞式
        pool.apply(func=Foo,args=(i,)) ##阻塞式
    pool.close()
    pool.join()
    pool.terminate()
    p_end =time.time()
    t = p_end - p_start
    print("the program time is :%s" %t)