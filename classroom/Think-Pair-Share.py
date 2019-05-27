class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = []

    def getName(self, name):
        return self.name

    def getAge(self, age):
        return self.age

    def setScore(self, count):
        ls = []
        for i in range(count):
            s = eval(input('Input Score: '))
            self.score.append(s)

    def getMaxScore(self):
        return max(self.score)


fx = Student('fx', 20)
fx.setScore(3)
print(fx.getMaxScore())
