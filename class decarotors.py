def attach_init(cls):
    def wrapper(self, a, b):
        self.a = a
        self.b = b
    cls.__init__ = wrapper
    return cls

