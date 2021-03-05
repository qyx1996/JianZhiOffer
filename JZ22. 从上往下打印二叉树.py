# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class Solution:
    def PrintFromTopToBottom(self, root):
        if not root: return []
        queue = [root]
        res = []
        while queue:    # 用队列实现，弹出最先进入的节点，记录节点值并将节点左右子节点推进队列
            if not queue: break
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
