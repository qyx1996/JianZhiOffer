class Solution:
    def isSymmetrical(self, pRoot):
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(R.left, L.right)

        return recur(pRoot.left, pRoot.right) if pRoot else True