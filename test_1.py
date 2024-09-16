def singleton(cls):
    def wrapper(*args,**kwargs):
        if not hasattr(cls,"instance_singleton"):
            setattr(cls,"instance_singleton",cls(*args,**kwargs))
        return getattr(cls,"instance_singleton")
    return wrapper