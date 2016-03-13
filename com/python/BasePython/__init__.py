class Person:
    __name = ""     #私有变量必须有二个下滑线开头
    __age = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age