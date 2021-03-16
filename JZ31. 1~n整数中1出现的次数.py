# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
# 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
# 可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）


class Solution:   # 重要！！！！！！！！ 根据当前位数的数字讨论
    def NumberOf1Between1AndN_Solution(self, n):
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res