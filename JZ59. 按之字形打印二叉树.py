class Solution:
    def Print(self, pRoot):
        if not pRoot: return []
        res, queue = [], [pRoot]
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp[::-1] if len(res) % 2 else temp)
        return res