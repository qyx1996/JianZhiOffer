# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
# 请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 方案1：
#
# 第一步：遍历老链表，构建正常的链表，用一个map（哈希表）记录p到new_p
# 第二步：新老链表同步next移动，对比记录random指针。
# p 1->2->3->4 map | | | | new_p 1->2->3->4
# 需要借助O(n)的空间，时间复杂度为o(n)
#
# 方案2：
#
# 不需要借助O(n)的空间，时间复杂度为o(n)
# 老新链表交叉存储，奇数位置为老链表，偶数位置新链表复制前一个位置。
# 新链表random即为旧链表random的后一个位置。
# p1->p1'->p2->p2'->...->pn->pn'
# 将两个链表分开，偶数位置的是新链表


# 1. using dictionary
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return
        cur, dic = pHead, {}
        # copy nodes
        while cur:
            dic[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = pHead
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[pHead]


# 2. copy and separate
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return
            # copy nodes
        cur = pHead
        while cur:
            nxt = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nxt
            cur = nxt
        # copy random pointers
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # separate two parts
        second = cur = pHead.next
        while cur.next:
            pHead.next = cur.next
            pHead = pHead.next
            cur.next = pHead.next
            cur = cur.next
        pHead.next = None
        return second
