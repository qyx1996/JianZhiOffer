class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            carry = (num1 & num2) << 1
            num1 = num1 ^ num2
            num2 = carry
        return num1