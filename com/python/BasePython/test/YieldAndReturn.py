# -*- coding:utf-8 -*-
def func(n):
    for i in range(n):
        yield i
if __name__=="__main__":
    print func(2) #仅仅是一个地址 并不是任何一个元素
    f = func(3)
    print f.next() #通过这种方式 访问元素 可见每次仅仅返回一个元素
