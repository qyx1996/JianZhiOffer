# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


class Solution:
    def reOrderArray(self, array):
        res = [0] * len(array)
        # 统计奇数个数
        odd_cnt = 0
        for n in array:
            if n % 2 != 0:
                odd_cnt += 1
        # 按奇数偶数填坑
        odd_i = 0
        even_i = odd_cnt
        for i in range(len(array)):
            if array[i] % 2 != 0:
                res[odd_i] = array[i]
                odd_i += 1
            else:
                res[even_i] = array[i]
                even_i += 1
        return res
