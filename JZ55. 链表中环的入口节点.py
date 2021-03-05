# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            print('error: List is empty')
        fast = slow = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:   # 快慢两指针可以相遇的话，说明存在环
                node = pHead
                while node != fast:   # 一个指针指向头节点，一个指向相遇点，两者一起出发，将在环的入口处相遇
                    fast = fast.next
                    node = node.next
                return node
        return None
