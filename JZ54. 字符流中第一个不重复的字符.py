class Solution:
    def __init__(self):
        self.data = []

    def FirstAppearingOnce(self):
        return self.data[0] if self.data else '#'

    def Insert(self, char):
        n = len(self.data)
        for i in range(n - 1, -1, -1):
            if self.data[i] == char:
                self.data.pop(i)
                return
        self.data.append(char)