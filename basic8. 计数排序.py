def countSort(arr):
    min = 2147483647
    max = 0
    # 取得最大值和最小值
    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x
    # 创建数组C
    count = [0] * (max - min +1)
    for index in arr:
        count[index - min] += 1
    index = 0
    # 填值
    for a in range(max - min+1):
        for c in range(count[a]):
            arr[index] = a + min
            index += 1
    return arr