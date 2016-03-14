class Person:
    age = 0
    __name = ""
    def __init__(self,age, name):
        self.age =age
        self.__name =name

if __name__ == "__main__":
    p = Person(10,"tcliuyong");
    print p.age