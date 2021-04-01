class Solution:
    def duplicate(self, numbers):
        if not numbers: return -1
        for index in range(len(numbers)):
            if numbers[index] == numbers[numbers[index]] and numbers[index] != index:
                return numbers[index]
            else:
                temp = numbers[index]
                numbers[index], numbers[temp] = numbers[temp], numbers[index]
        return -1