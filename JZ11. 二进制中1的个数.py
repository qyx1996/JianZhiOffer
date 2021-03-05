# 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。


from ctypes import *


class Solution:
    def NumberOf1(self, n):
        cnt = 0
        while c_int(n).value:    # 每做一次n-1和n的位与运算，可以将n的最后一个1变为0
            n = n & (n - 1)      # 因此我们判断 n-1 & n 能够循环运行的次数就可以判断二进制中有多少个1了。
            cnt += 1
            print(c_int(n), n)
        return cnt

# 另一种思路：将1不断左移并和n进行位与运算，当两者位与结果为1时说明该位置有1，则count+1，最后输出count

A = Solution()
print(A.NumberOf1(-1))