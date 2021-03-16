# 输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
# 最长路径的长度为树的深度。


# 递归
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot: return 0
        if not pRoot.left and not pRoot.right:
            return 1
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))


# 循环
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        queue = [pRoot]
        depth = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth += 1
        return depth