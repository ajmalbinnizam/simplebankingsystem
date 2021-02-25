class DemoClass:
    def __init__(self, sum):
        self.num = 100
        self.sum = sum

    def read_num(self):
        print(self.num)

    def sum_num(self):
        s = self.sum+self.sum
        print(s)


obj = DemoClass(5)
obj.read_num()
obj.sum_num()