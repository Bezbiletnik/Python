class MyClass():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def status(self):
        return self.count

obj = MyClass()
print(obj.status())
obj.increment()
print(obj.status())
