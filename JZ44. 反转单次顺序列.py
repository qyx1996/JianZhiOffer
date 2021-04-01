# 直接调用API
class Solution:
    def ReverseSentence(self, s):
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回


# 双指针寻找各单次的首尾字符
class Solution:
    def ReverseSentence(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
