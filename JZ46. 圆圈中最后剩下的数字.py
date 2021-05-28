# 循环法
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        n = list(range(n))
        if not n: return -1
        i = 0
        while len(n) != 1:
            for _ in range(m-1):
                i += 1
                i %= len(n)
            n.pop(i)
        return n



# 数学法
# f(n)
# =(f(n−1)+t)%n
# =(f(n−1)+m%n)%n
# =(f(n−1)+m)%n
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x