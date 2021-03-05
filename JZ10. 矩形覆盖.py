# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 比如n=3时，2*3的矩形块有3种覆盖方法：


class Solution:
    def rectCover(self, number):
        if number == 1: return 1
        elif number == 2: return 2
        elif number >= 3:
            prev = 1
            next = 2
            for _ in range(number - 2):
                prev, next = next, prev + next
            return next
        else:
            return 0
