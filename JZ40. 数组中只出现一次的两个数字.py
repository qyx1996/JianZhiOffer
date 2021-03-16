# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。


class Solution:
    def FindNumsAppearOnce(self , array ):
        x, y, n, m = 0, 0, 0, 1
        for num in array:  # 1. 遍历异或
            n ^= num
        while n & m == 0:  # 2. 循环左移，计算 m
            m <<= 1
        for num in array:  # 3. 遍历 array 分组
            if num & m:
                x ^= num  # 4. 当 num & m != 0
            else:
                y ^= num  # 4. 当 num & m == 0
        return [x, y] if x < y else [y, x] # 5. 返回出现一次的数字
