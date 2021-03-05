# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。n≤39


# 递归
class Solution:
    def Fibonacci(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        else:
            return self.Fibonacci(n - 2) + self.Fibonacci(n - 1)


# 循环
class Solution:
    def Fibonacci(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        else:
            Fibonacci_first = 0
            Fibonacci_second = 1
            i = 2
            while i <= n:
                Fibonacci_result = Fibonacci_first + Fibonacci_second
                Fibonacci_first = Fibonacci_second
                Fibonacci_second = Fibonacci_result
                i += 1
            return Fibonacci_result

A = Solution()
print(A.Fibonacci(4))