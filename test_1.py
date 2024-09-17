def singleton(cls):
    def wrapper(*args,**kwargs):
        if not hasattr(cls,"instance_singleton"):
            setattr(cls,"instance_singleton",cls(*args,**kwargs))
        return getattr(cls,"instance_singleton")
    return wrapper


@singleton
class Test():
    def __init__(self):
        pass

print("wjc——test")

if __name__ == "__main__":
    a = Test()
    b = Test()
    print(a)
    print(b)