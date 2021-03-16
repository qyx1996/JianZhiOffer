# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 1: return index
        res = [1] * index
        i2, i3, i5 = 0, 0, 0
        for i in range(1, index):
            res[i] = min(res[i2] * 2, min(res[i3] * 3, res[i5] * 5))
            if res[i] == res[i2] * 2: i2 += 1
            if res[i] == res[i3] * 3: i3 += 1
            if res[i] == res[i5] * 5: i5 += 1
        return res[-1]