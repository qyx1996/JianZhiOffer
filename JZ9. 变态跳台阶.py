# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


# 循环
class Solution:
    def jumpFloorII(self, number):
        f1 = 1
        if number == 1: return f1
        for _ in range(number - 1):
            f1 = 2 * f1
        return f1
