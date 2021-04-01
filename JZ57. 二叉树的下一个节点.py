class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: return None
        p = pNode
        if pNode.right:  # 若有右子树，则下一个节点是右子树的最左下子节点
            p = pNode.right
            while p.left:
                p = p.left
            return p
         # 没有右子树但是有父亲节点，若是父节点的左子节点，则下一节点就是父节点
         # 若是父节点的右子节点，则需要一直向上，直到某个节点是其父节点的左子节点，则该节点的父节点是结果
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next