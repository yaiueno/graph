class MyClass:
    def __init__(self,val):
        self.val = val
    def output(self):
        print('val = {}'.format(self.val))
myClass = MyClass(45)
myClass.output()