# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。


# 递归方法
class Solution:
    def Convert(self, pRootOfTree):
        # 二叉树排序  中序遍历
        # 1. 确定链表起始节点   一直 向左走 第一个左节点为空的节点为链表的起始节点
        # 2. root.left = func(root.left)
        # 3. root.right = pre  更新记录pre节点
        self.pre = None
        self.root = None
        self.convert(pRootOfTree)
        return self.root

    def convert(self, root):
        if not root:
            return None

        self.convert(root.left)
        if not self.root:
            self.root = root
        if self.pre:
            root.left = self.pre
            self.pre.right = root
        self.pre = root
        self.convert(root.right)


# 循环方法，中序遍历二叉树 !!!暂时有问题
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree: return
        dummy = TreeNode(0)    # 初始化头节点
        prev = dummy                   # pre记录前一个节点
        stack, node = [], pRootOfTree  # 用stack进行中序遍历
        while stack or node:
            while node:                # 遍历node左子树
                stack.append(node)
                node = node.left
            node = stack.pop()         # 该node是当前栈内最小值
            node.left, prev.right, prev = prev, node, node      # node左指针指向prev，prev右指针指向node，将当前node记录为prev
            node = node.right          # 遍历node右子树
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
