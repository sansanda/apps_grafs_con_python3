def decorator(fn):
    def wrapper(*args, **kwargs):
        print("Look, I've added something here!")
        return fn(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    return a + b

res = add(1, 2)
print(res)

