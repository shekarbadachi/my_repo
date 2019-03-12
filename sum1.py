class Add:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def calc(self):
        sm = self.v1 + self.v2
        return sm


if __name__ == "__main__":
    n1, n2 = [int(x) for x in raw_input('enter two values').split()]
    sum1 = Add(n1, n2)
    print " {} + {} = {}".format(n1, n2, sum1.calc())
