# 给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，
# 则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k <= 0:
            return []
        start, end = 0, len(tinput) - 1
        index = self.partition(tinput, start, end)  # 快排，若index等于k-1，则前k-1个数都比后面的数小
        while index != k - 1:
            if index < k - 1:
                index = self.partition(tinput, index + 1, end)
            if index > k - 1:
                index = self.partition(tinput, start, index -1)
        return tinput[:k]

    def partition(self, nums, start, end):  # 快速排序
        pivot = nums[end]
        small = start - 1
        for index in range(start, end):
            if nums[index] <= pivot:
                small += 1
                nums[small], nums[index] = nums[index], nums[small]
        nums[small + 1], nums[end] = nums[end], nums[small + 1]
        return small + 1

    # def partition(self, nums, start, end):
    #     pivot = nums[start]
    #     while start < end:
    #         while start < end and nums[end] >= pivot:
    #             end -= 1
    #         nums[start] = nums[end]
    #         while start < end and nums[start] < pivot:
    #             start += 1
    #         nums[end] = nums[start]
    #     nums[start] = pivot
    #     return start


A = Solution()
print(A.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))
print(A.GetLeastNumbers_Solution([-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8], 4))
