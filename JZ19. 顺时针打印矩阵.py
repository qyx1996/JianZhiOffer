# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字


class Solution:
    def printMatrix(self, matrix):
        walked = [[False] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for j in range(len(walked[-1])):
            walked[-1][j] = True
        for i in range(len(walked)):
            walked[i][-1] = True

        len_row = len(matrix) - 1
        len_col = len(matrix[0]) - 1
        res = []
        i = 0
        j = 0
        direction = 0  # 0向右，1向下，2向左，3向上

        while not walked[i][j]:
            res.append(matrix[i][j])
            walked[i][j] = True
            if direction == 0:  # 向右
                if j < len_col and not walked[i][j + 1]:
                    j += 1
                else:
                    direction = 1 # 到头了，向下转弯
                    i += 1
            elif direction == 1:  # 向下
                if i < len_row and not walked[i + 1][j]:
                    i += 1
                else:
                    direction = 2 # 到头了，向左转弯
                    j -= 1
            elif direction == 2:  # 向左
                if j > 0 and not walked[i][j - 1]:
                    j -= 1
                else:
                    direction = 3 # 到头了，向上转弯
                    i -= 1
            elif direction == 3:  # 向上
                if i > 0 and not walked[i - 1][j]:
                    i -= 1
                else:
                    direction = 0 # 到头了，向右转弯
                    j += 1
        return res