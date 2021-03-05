# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）


class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        pop_index = 0
        for number in pushV:     # 遍历pushV里的所有元素
            stack.append(number)
            while stack and stack[-1] == popV[pop_index]:   # 若stack顶部元素与popV当前元素相同，则从stack中pop
                pop_index += 1
                stack.pop()
        if not stack:    # 若最后stack为空，则是弹出序列
            return True
        else:
            return False
