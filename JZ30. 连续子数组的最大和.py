# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。要求时间复杂度为 O(n).


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array: return 0
        max_sum = -float('inf')
        cur_sum = 0
        for num in array:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


A = Solution()
print(A.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))