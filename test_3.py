def repeat(times):
    def repeat_helper(func):
        def call_helper(*args):
            for i in range(0,times):
                func(*args)
        return call_helper
    return repeat_helper

import time
def calc_time(func):
    def wapper_calc(*args):
        start = time.time()
        func(*args)
        end = time.time()
        cost_time = end - start
        print("function名字"+func.__name__ +"共耗时"+str(cost_time))
    return wapper_calc


@repeat(5)
def test_w(name):
    print(name)
@calc_time
def test_w2(name):
    time.sleep(2)
    print(name)

if __name__ == "__main__":
    # test_w("wjc")
    test_w2("wjc")