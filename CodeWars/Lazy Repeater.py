def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

@call_counter
def make_looper(string):
    print(make_looper.calls())
    return string[make_looper.calls % len(string)]


make_looper('abc')
# @call_counter
# def f():
#     pass

# print(f.calls())