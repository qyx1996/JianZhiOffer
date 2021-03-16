# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        lp = 0
        rp = len(array) - 1
        res = [array[-1]] * 2
        while lp < rp:
            tmp = array[lp] + array[rp]
            if tmp > tsum:
                rp -= 1
            elif tmp < tsum:
                lp += 1
            else:
                if array[lp] * array[rp] < res[0] * res[1]:
                    res[0], res[1] = array[lp], array[rp]
                lp += 1
                rp -= 1

        return res if res[0] + res[1] == tsum else []