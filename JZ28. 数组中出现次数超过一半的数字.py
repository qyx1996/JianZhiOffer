# 数组中有一个数字出现的次数超过数组长度的一半，
# 请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return None
        res, count = None, 0
        for num in numbers:
            if not res:
                res, count = num, 1
            else:
                if num == res:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        res = None     # 将不同的数字消去，最后剩下的就是出现次数大于一半的（存在出现次数超过一半的情况下）

        count = 0  # 判断该数字出现次数是否大于一半
        for num in numbers:
            if num == res:
                count += 1
        if count > len(numbers) / 2:
            return res
        else:
            return 0
