# 在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007


class Solution:
    def InversePairs(self, data):
        def merge_sort(left, right):
            # 终止条件
            if left >= right: return 0
            # 递归划分
            mid = (left + right) // 2
            res = merge_sort(left, mid) + merge_sort(mid + 1, right)
            # 合并阶段
            left_index, right_index = left, mid + 1
            tmp[left: right + 1] = data[left: right + 1]
            for index in range(left, right + 1):
                if left_index == mid + 1:     # 左序列到头了，剩下的全是右序列
                    data[index] = tmp[right_index]
                    right_index += 1
                elif right_index == right + 1 or tmp[left_index] <= tmp[right_index]:   # 左序列的数比右序列小，或者右序列到头了
                    data[index] = tmp[left_index]
                    left_index += 1
                else:              # 左序列的数比右序列大，此时需要计算逆序对数量
                    data[index] = tmp[right_index]
                    right_index += 1
                    res += mid - left_index + 1  # 统计逆序对，数量等于左序列中剩余的数字个数
            return res

        tmp = [0] * len(data)
        return merge_sort(0, len(data) - 1) % 1000000007
