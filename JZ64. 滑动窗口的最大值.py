class Solution:
    def maxInWindows(self, num, size):
        if size > len(num) or size == 0:
            return []
        queue, res = [], []
        for i in range(len(num)):
            while queue and queue[0] <= i - size:     # 当队列第一个数超出窗口范围时弹出
                queue.pop(0)
            while queue and num[queue[-1]] < num[i]:  # 当队列最后一个数小于当前数时弹出
                queue.pop(-1)
            queue.append(i)
            # if i < size - 1:
            #     continue
            # res.append(num[queue[0]])
            if i >= size - 1:
                res.append(num[queue[0]])
        return res


A = Solution()
print(A.maxInWindows([2,3,4,2,6,2,5,1], 3))