import os


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性
        print('{}出生了！'.format(self.name))

    def getAge(self):
        print('------{}------'.format(self.__age))

    def __setAge(self):     # 私有方法
        self.__age = 18
        print('New age is {}'.format(self.__age))

    def setAge(self):       # 接口
        self.__setAge()

    def __del__(self):
        print('啊，{}死了！'.format(self.name))


laowang = Person('老王', 30)
laowang.getAge()
laowang.setAge()
print('开枪打老王')
del laowang
print('over')

xiaoming = Person('小明', 20)
xiaohong = xiaoming     # 硬链接
print('开枪打小明')
del xiaoming
print('del 小明，但小明没死')
print('再次开枪打小明')
del xiaohong
print('over2')
