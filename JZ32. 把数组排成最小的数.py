# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。
# 不会做！！！！！！


class Solution:
    def PrintMinNumber(self, numbers):
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while numbers[j] + numbers[l] >= numbers[l] + numbers[j] and i < j: j -= 1
                while numbers[i] + numbers[l] <= numbers[l] + numbers[i] and i < j: i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
            numbers[i], numbers[l] = numbers[l], numbers[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        numbers = [str(num) for num in numbers]
        quick_sort(0, len(numbers) - 1)
        return ''.join(numbers)