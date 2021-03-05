# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


class Solution:
    def replaceSpace(self , s ):
        res = ''
        str = ''
        for str in s:
            if str == ' ':
                res += '%20'
            else:
                res += str
        return res

A = Solution()
s = "We Are Happy"
# s = "We"
print(A.replaceSpace(s))