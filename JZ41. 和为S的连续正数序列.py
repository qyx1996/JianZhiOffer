class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        windows = []
        sum = 0
        for t in range(1, tsum):
            windows.append(t)
            sum += t
            while sum > tsum:
                sum -= windows.pop(0)
            if sum == tsum:
                res.append(windows[:])

        return res


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res