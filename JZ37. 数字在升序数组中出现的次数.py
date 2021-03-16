# 统计一个数字在升序数组中出现的次数。


class Solution:
    def biSearch(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
        return high

    def GetNumberOfK(self, data, k):
        if not data: return 0
        return self.biSearch(data, k + 0.5) - self.biSearch(data, k - 0.5)