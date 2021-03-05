# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class Solution:
    def deleteDuplication(self, pHead):
        head = ListNode(0)
        head.next = pHead
        pre = head
        post = head.next
        while post and post.next:
            if post.next.val == post.val:
                while post.next and post.next.val == post.val:
                    post.next = post.next.next
                pre.next = post.next
                post = pre.next
            else:
                pre = post
                post = post.next
        return head.next
