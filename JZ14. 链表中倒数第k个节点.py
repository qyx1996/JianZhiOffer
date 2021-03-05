# 输入一个链表，输出该链表中倒数第k个结点。


class Solution:
    def FindKthToTail(self, pHead, k):
        if not pHead:
            print('error: List is empty')
            return
        else:
            if k <= 0:
                print('error: k should be positive')
                return
            else:
                fast = slow = pHead
                for _ in range(k):
                    if not fast:
                        print('error: k is larger than length')
                        return
                    fast = fast.next
                while fast:
                    fast, slow = fast.next, slow.next
                return slow
