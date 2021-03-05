# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。


class Solution:
    def __init__(self):
        self.stack = []
        self.minimal = []

    def push(self, node):
        self.stack.append(node)
        if not self.minimal:
            self.minimal.append(node)
        else:
            self.minimal.append(min(node, self.minimal[-1]))

    def pop(self):
        if self.stack and self.minimal:
            self.minimal.pop()
            return self.stack.pop()
        else:
            return []

    def top(self):
        if self.stack: return self.stack[-1]
        else: return []

    def min(self):
        if self.minimal: return self.minimal[-1]
        else: return []