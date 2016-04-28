# -*- coding:utf-8 -*-
import os
def visitdir(path):
    dirs = []
    localdirs = os.listdir(path)
    for d in localdirs:
        pathname = os.path.join(path,d)
        if not os.path.isfile(pathname):
            visitdir(pathname)
        else:
            dirs += pathname
    return  dirs

