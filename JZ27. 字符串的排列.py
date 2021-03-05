# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


class Solution:
    def helper(self, s):
        if len(s) == 1:
            return s[0]
        res = []
        for i in range(len(s)):
            l = self.helper(s[:i] + s[i + 1:])
            for j in l:
                res.append(s[i] + j)             # 递归得到将第i个字符置于首位时的所有排列
        return res

    def Permutation(self, ss):
        if not ss: return []
        words = list(ss)
        return list(sorted(set(self.helper(words))))   # 利用python的set功能消除重复，sorted按字典排序
