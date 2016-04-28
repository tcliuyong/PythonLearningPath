# -*- coding:utf-8 -*-
class Shop:
   shopName = ""
   score = 0
   userName = ""
   content=""
   level=""
   def __init__(self, shopName = "", score = 0, userName = "test", content = "xxx", level = "0"):
       self.shopName =shopName
       self.score =score
       self.userName =userName
       self.content =content
       self.level =level
