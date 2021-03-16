# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）


class Solution:
    def FirstNotRepeatingChar(self, s):
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1
