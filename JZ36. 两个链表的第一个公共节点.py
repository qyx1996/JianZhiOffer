# 输入两个链表，找出它们的第一个公共结点。
# （注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）


class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        p1, length1 = pHead1, 0
        p2, length2 = pHead2, 0
        while p1:
            p1 = p1.next
            length1 += 1
        while p2:
            p2 = p2.next
            length2 += 1
        if length1 < length2:  # p1指向长链
            pHead1, pHead2 = pHead2, pHead1
            length1, length2 = length2, length1

        for _ in range(length1 - length2):
            pHead1 = pHead1.next
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return None