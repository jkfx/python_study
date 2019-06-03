import random


class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def run(self, km):
        print("---跑---")
        if km >= 5:
            self.weight -= 2

    def eat(self):
        print("---吃---")

    def isHungary(self, hungary):
        if hungary:
            self.eat()
        else:
            print("---不饿---")

    def sleep(self):
        print("---睡---")