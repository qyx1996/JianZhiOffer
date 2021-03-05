# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2: return False
        if self.ifEqual(pRoot1, pRoot2): return True
        else: return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        # 递归检测root2是否是root1左子树和右子树的子结构

    def ifEqual(self, Tree1, Tree2):     # 检查从Tree1和Tree2开始的两棵树是否子节点都相等
        if not Tree2: return True
        elif not Tree1: return False
        elif Tree1.val != Tree2.val: return False  # 这里有个问题，如果都是double型，则不能随便用!=符号
        else: return self.ifEqual(Tree1.left, Tree2.left) and self.ifEqual(Tree1.right, Tree2.right)
