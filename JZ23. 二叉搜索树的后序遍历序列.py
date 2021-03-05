# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence: return False
        return self.helper(sequence)

    def helper(self, sequence):
        if len(sequence) <= 1:
            return True
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        return self.helper(sequence[:i]) and self.helper(sequence[i:-1])
