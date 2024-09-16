def repeat(times):
    def repeat_helper(func):
        def call_helper(*args):
            for i in range(0,times):
                func(*args)
        return call_helper
    return repeat_helper

@repeat(5)
def test_w(name):
    print(name)

if __name__ == "__main__":
    test_w("wjc")