# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


# 递归
class Solution:
    def jumpFloor(self, number):
        if number == 1: return 1
        if number == 2: return 2
        if number >= 3:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


# 循环
class Solution:
    def jumpFloor(self, number):
        if number == 1: return 1
        if number == 2: return 2
        if number >= 3:
            prev_prev = 1
            prev = 2
            i = 3
            while i <= number:
                prev_prev, prev = prev, prev + prev_prev
                i += 1
            return prev
