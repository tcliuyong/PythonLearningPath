# -*- coding:utf-8 -*-
import shutil
import os
class docoperation:
    __src = ""
    __dest = ""
    # def __init__(self, src, dest):
    #     self.__dest = dest
    #     self.__src = src

    def copyfile(self, src, dest):
        shutil.copy(src, dest)
    def updatesuffix(self, dir, suffix1, suffix2):
        files = os.listdir(dir)
        for file in files:
            pos = file.find(".")
            if(file[pos + 1:]) == suffix1:
                newname = file[:pos + 1] + suffix2
                print newname
                os.rename(dir + "//"+file,dir + "//"+newname)



