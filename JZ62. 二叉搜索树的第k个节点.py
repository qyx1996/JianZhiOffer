# 给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点。


class Solution:
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        stack = []
        while pRoot or stack:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop()
            k -= 1
            if k == 0:
                return pRoot
            pRoot = pRoot.right


# 找出第k大的值
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


# 找出第k小的值
class Solution:

    def KthNode(self, root, k):
        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.right)

        self.k = k
        dfs(root)
        return self.res
