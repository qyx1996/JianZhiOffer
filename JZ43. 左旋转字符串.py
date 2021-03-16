# 第一种
class Solution:
    def LeftRotateString(self, s, n):
        if not s: return ''
        n = n % len(s)
        return s[n:] + s[:n]


# 第二种
class Solution:
    def LeftRotateString(self, s, n):
        if not s: return ''
        res = ''
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res


# 第二种
class Solution:
    def LeftRotateString(self, s, n):
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res
