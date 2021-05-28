# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

class Solution:
    # 解法1：栈
    def printListFromTailToHead(self, listNode):
        stack = []
        res = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            res.append(stack.pop())
        return res

    # 解法2：递归
    result_array = []

    def printListFromTailToHead(listNode):
        # write code here
        if listNode:
            printListFromTailToHead(listNode.next)
            result_array.append(listNode.val)
        return result_array