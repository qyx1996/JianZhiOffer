# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        col = -1
        for row in array:
            while col + len(row) and row[col] > target:
                col -= 1
            if row[col] == target:
                return True
        return False

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols= len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False

A = Solution()
array = [[2,4,5,8,9,12,15,18,19,21],[5,7,8,10,13,16,18,20,21,24],[7,9,11,12,14,19,22,24,25,28],[8,10,14,17,19,22,23,27,30,32],[10,12,16,20,22,25,27,30,32,35],[11,13,17,23,25,28,31,32,35,38],[13,16,18,24,27,30,34,36,39,40],[14,19,22,26,30,32,37,39,42,45],[15,21,25,29,33,34,40,43,44,47],[16,23,27,32,35,37,43,45,47,50]]
target = 5
print(A.Find(target, array))