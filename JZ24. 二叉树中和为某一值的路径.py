# 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


class Solution:
    def __init__(self):
        self.result_all = []      # 用来保存结果的list
        self.array = []           # 用来保存路径的栈

    def FindPath(self, root, expectNumber):
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.array.pop()         # 遍历完一个节点后弹出子节点（叶节点、或叶节点已经被完全遍历的父节点）
        return self.result_all