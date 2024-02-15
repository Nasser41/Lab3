def repeat_decorator(repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(repetitions):
                func()
        return wrapper
    return decorator

x = int(input("Enter a number of repetitions: "))

@repeat_decorator(x)
def hello():
    print("hello")

hello()