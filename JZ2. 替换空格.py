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