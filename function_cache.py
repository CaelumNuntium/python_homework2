class FunctionCache(object):
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache.keys():
            print(f"Using cached value for argument {args}")
        else:
            self.cache[args] = self.function(*args)
        return self.cache[args]


def power(x, y):
    return x ** y


power_cached = FunctionCache(power)
print(power_cached(2, 2))
print(power_cached(4, 2))
print(power_cached(4, 2))
print(power_cached(2, 2))
