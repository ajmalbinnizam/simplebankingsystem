class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def area(self):
        if int(self.c) ** 2 != int(self.a) ** 2 + int(self.b) ** 2:
            print('Not right')
        else:
            s = .5 * int(self.a) * int(self.b)
            print(s)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here

angle = RightTriangle(input_c, input_a, input_b)
angle.area()