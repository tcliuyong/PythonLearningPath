# coding=utf-8
import math
class sample(object):
    moment1Sum = 0.0 #二阶原点矩和
    moment2Sum = 0.0 #二阶原点矩和
    moment3Sum = 0.0 #三阶原点矩和
    moment4Sum = 0.0 #四阶原点矩和
    __n = 0
    __arr = []
    mean = 0.0 #均值
    mean2 = 0.0 #均值的二次方
    def __init__(self, arr):
        self.__arr = arr
        self.__n = len(arr)
        for i in range(self.__n):
            self.moment1Sum = self.moment1Sum + self.__arr[i]
            self.moment2Sum = self.moment2Sum + math.pow(self.__arr[i], 2.0)
            self.moment3Sum = self.moment3Sum + math.pow(self.__arr[i], 3.0)
            self.moment4Sum = self.moment4Sum + math.pow(self.__arr[i], 4.0)
            self.mean = self.moment1Sum / self.__n
            self.mean2 = math.pow(self.mean, 2.0)
    def calMedia(self):
        media = 0
        sorted_list = sorted(self.__arr)
        mid = self.__n / 2
        if self.__n % 2 == 0:
            media = (sorted_list[mid] + sorted_list[mid - 1]) / 2
        else:
            media = sorted_list[mid]
        return media
    #计算方差
    def calVariance(self):
        variance = 0.0
        if(self.mean == None):
            return 0.999
        for i in range(self.__n):
            variance = variance + (self.__arr[i] - self.mean) * (self.__arr[i]- self.mean)
        return variance / self.__n
    #计算变异系数
    def calCV(self):
        cv = 0.0
        variance= self.calVariance()
        cv = math.sqrt(variance) / self.mean
        return cv
    #计算2阶原点矩
    def Moment2(self):
        return self.moment2Sum / self.__n
    #计算3阶原点矩
    def Moment3(self):
        return self.moment3Sum / self.__n
    #计算4阶原点矩
    def Moment4(self):
        return self.moment4Sum / self.__n
    #2阶中心距 也就是方差
    def calCenterMoment2(self):
        centerMoment2 = (self.moment2Sum - self.moment1Sum * self.mean) / self.__n
        return centerMoment2
    #3阶中心距
    def calCenterMoment3(self):
        centerMoment3 = self.moment3Sum - 3 * self.mean * self.moment2Sum + 2 * self.moment1Sum * self.mean2
        return centerMoment3
    #4阶中心距
    def calCenterMoment4(self):
        centerMoment3 = self.calCenterMoment3()
        centerMoment2 = self.calCenterMoment2()
        centerMoment4 = centerMoment3 / math.pow(centerMoment2, 1.5)
        return centerMoment4
    #计算三本峰度
    def calKurtosis(self):
        centerMoment3 = self.calCenterMoment3()
        centerMoment2 = self.calCenterMoment2()
        centerMoment4 = centerMoment3 / math.pow(centerMoment2, 1.5)
        kurtosis = centerMoment4/(centerMoment2 * centerMoment2)
        return kurtosis - 3