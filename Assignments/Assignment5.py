def output_decorator(name):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)

            print("############################")
            print("#", name)
            print("# input: ", ",".join(map(str, args)))
            print("# output: ", result)
            print("############################")
            return result
        return wrapper
    return decorator

@output_decorator("Addition")
def add(a,b):
    return a + b

add(3,4)