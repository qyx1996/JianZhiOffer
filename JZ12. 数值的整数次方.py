# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 保证base和exponent不同时为0


class Solution:
    def Power(self, base, exponent):
        if exponent == 0: return 1
        flag = 1
        if exponent < 0:
            exponent *= -1
            flag = 0
        temp = base
        res = 1
        while exponent:
            if exponent & 1:
                res *= temp
            temp *= temp
            exponent = exponent >> 1

        return res if flag else 1.0 / res
