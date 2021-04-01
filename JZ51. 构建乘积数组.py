# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if len(A) <= 1:
            return []
        B = [1] * len(A)

        temp = 1
        for i in range(1, len(A)):
            temp *= A[i - 1]
            B[i] *= temp

        temp = 1
        for i in range(len(A) - 2, -1, -1):
            temp *= A[i + 1]
            B[i] *= temp
        return B