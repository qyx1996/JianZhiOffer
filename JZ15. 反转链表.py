# 输入一个链表，反转链表后，输出新链表的表头。


# 循环
class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return None

        prev, Node = None, pHead   # prev指向上一个节点，Node指向当前节点

        while Node:
            post = Node.next       # post指向下一个节点，保存节点防止断裂
            Node.next = prev       # 将当前节点next指向上一个节点，完成反转
            prev = Node            # 将prev指针后移一位（指向当前节点的位置）
            Node = post            # 将Node指针后移一位（指向刚才存储的post位置）

        return prev

# 简化的循环
class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return None
        prev, Node = None, pHead
        while Node:
            Node.next, prev, Node = prev, Node, Node.next
        return prev


# 递归
class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        node = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return node