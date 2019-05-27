class Cat(object):

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def run(self):
        print('-----跑-----')

    # def __del__(self):
        # print('-----death----')


class Bosi(Cat):

    def eat(self):
        print('-----吃-----')


class Jiafei(Cat):

    def drink(self):
        print('-----喝-----')


bosi = Bosi('波斯猫', '白色', 15)
bosi.run()
bosi.eat()
print(bosi.name, bosi.color, bosi.weight)
