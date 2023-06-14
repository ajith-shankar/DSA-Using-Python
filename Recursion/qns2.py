class Demo:
    def __init__(self, num1, num2):
        self.val = num1=num2

class Demo1(Demo):
    def __int__(self, num1, num2):
        self.val = num1 - num2
        super().__init__(num1, num2)

obj1 = Demo1(20, 10)
obj2 = Demo(20, 10)
print(obj1. val)
print(obj2.val)