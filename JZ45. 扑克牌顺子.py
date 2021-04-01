class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return None
        numbers.sort()
        n_zero, i = 0, 0
        while numbers[i] == 0:
            n_zero += 1
            i += 1
        number_of_gap = 0
        for index in range(n_zero, len(numbers) - 1):
            if numbers[index] == numbers[index + 1]:
                return False
            number_of_gap += numbers[index + 1] - numbers[index] - 1
        return True if number_of_gap <= n_zero else False


# 简洁版
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return 0
        numbers.sort()
        cnt = 0
        jokers = 0
        pre = None
        for i in range(len(numbers)):
            if numbers[i] == 0:
                jokers += 1
            else:
                if pre is None:
                    pre = numbers[i]
                else:
                    if pre == numbers[i]: return 0
                    cnt += numbers[i] - pre - 1
                    pre = numbers[i]
        cnt -= jokers
        return cnt <= 0


A = Solution()
print(A.IsContinuous([0,3,2,6,4]))
