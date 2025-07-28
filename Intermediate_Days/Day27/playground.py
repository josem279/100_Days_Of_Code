# Args
def add(*args):
    res = 0
    for n in args:
        res += n
    return res

# print(add(1,4,6,7,))

# kwargs
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # for key, val in kwargs.items():
    #     print(f"key:{key} - val:{val}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)