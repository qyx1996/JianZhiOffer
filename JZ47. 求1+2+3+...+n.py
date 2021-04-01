# 1.用n=1来终止递归
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


# python中and为真时返回后一个表达式的值
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))