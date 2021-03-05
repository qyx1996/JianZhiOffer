# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。


# 新建一个链表按大小存储
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1: return pHead2
        if not pHead2: return pHead1

        head, Node1, Node2 = ListNode(0), pHead1, pHead2
        Node = head
        while Node1 and Node2:
            if Node1.val < Node2.val:
                Node.next = Node1
                Node1 = Node1.next
                Node = Node.next
            else:
                Node.next = Node2
                Node2 = Node2.next
                Node = Node.next
        if Node1:
            Node.next = Node1
        if Node2:
            Node.next = Node2
        return head.next


# 递归
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        if pHead1.val < pHead2.val:
            merge_head = pHead1
            merge_head.next = self.Merge(pHead1.next, pHead2)
        else:
            merge_head = pHead2
            merge_head.next = self.Merge(pHead1, pHead2.next)
        return merge_head