# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
# 平衡二叉树（Balanced Binary Tree），具有以下性质：
# 它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
# 并且左右两个子树都是一棵平衡二叉树。


# 递归（从顶至底）
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot: return True
        return abs(self.depth(pRoot.left) - self.depth(pRoot.right)) <= 1 and \
               self.IsBalanced_Solution(pRoot.left) and \
               self.IsBalanced_Solution(pRoot.right)

    def depth(self, pRoot):
        if not pRoot: return 0
        return max(self.depth(pRoot.left), self.depth(pRoot.right)) + 1


# 从底置顶 剪枝
class Solution:
    def IsBalanced_Solution(self, pRoot):
        def recur(pRoot):
            if not pRoot: return 0
            left = recur(pRoot.left)
            if left == -1: return -1
            right = recur(pRoot.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return recur(pRoot) != -1
