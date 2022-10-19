class FunctionCache(object):
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, arg):
        if arg in self.cache.keys():
            print(f"Using cached value for argument {arg}")
        else:
            self.cache[arg] = self.function(arg)
        return self.cache[arg]


def square(x):
    return x ** 2


square_cached = FunctionCache(square)
print(square_cached(2))
print(square_cached(4))
print(square_cached(4))
