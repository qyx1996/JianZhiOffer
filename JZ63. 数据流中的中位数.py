# 用排序的数列实现，插入复杂度O(n)，得到中位数复杂度O(1)
class Solution:
    def __init__(self):
        self.sortedList = []

    def Insert(self, num):
        # write code here
        n = len(self.sortedList)
        self.sortedList.append(num)
        while n != 0:
            if self.sortedList[n] < self.sortedList[n-1]:     # 冒泡排序
                self.sortedList[n], self.sortedList[n-1] = self.sortedList[n-1], self.sortedList[n]
            else:
                break
            n -= 1
        if n == 0:
            self.sortedList[n] = num

    def GetMedian(self, x):
        # write code here
        n = len(self.sortedList)
        if n % 2 == 0:
            return (self.sortedList[n//2]+self.sortedList[n//2-1]) / 2.0
        else:
            return self.sortedList[n//2]


# 用最大堆和最小堆实现，heapq是最小堆，可以将元素取负存入最小堆，使用时再取正，即可实现最大堆
from heapq import *


class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
            # heappush(self.B, -heappushpop(self.A, num))    # 以上两句可用这一句替代，效率更高
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
            # heappush(self.A, -heappushpop(self.B, -num))   # 以上两句可用这一句替代，效率更高

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
