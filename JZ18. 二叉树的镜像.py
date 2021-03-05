# 操作给定的二叉树，将其变换为源二叉树的镜像。


# 递归
class Solution:
    def Mirror(self, pRoot):
        if not pRoot:
            return
        pRoot.left, pRoot.right = self.Mirror(pRoot.right), self.Mirror(pRoot.left)
        return pRoot


# 循环
import collections


class Solution:
    def Mirror(self, pRoot):
        queue = collections.deque([pRoot])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return pRoot