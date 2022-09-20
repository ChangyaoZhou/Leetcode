def sumOddLengthSubarrays(arr):
    # 【法一】暴力解法 时间复杂度 O(n^3)
    # 其中n是数组arr的长度，长度为奇数的子数组的数量是 O(n^2)，对于每个子数组需要O(n)的时间计算子数组的和，
    # 因此总时间复杂度是 O(n^3)

    # 【法二】前缀和 时间复杂度 O(n^2)
    # 法一中对于每个子数组需要使用 O(n)的时间计算子数组的和。如果能将计算每个子数组的和的时间复杂度从O(n)降低到O(1)，
    # 总时间复杂度就可以从O(n^3)降低到 O(n^2)
    # 可以先算出前缀和，计算长度为奇数的子数组元素和时可以直接使用
    pre_sum = [0 for _ in range(len(arr)+1)]
    for i in range(len(arr)):
        pre_sum[i+1] = pre_sum[i] + arr[i]

    result = 0
    for length in range(1, len(arr)+1, 2):  # 先遍历可能的奇数长度
        for j in range(0, len(arr) - length + 1):  # 遍历起点
            result += pre_sum[j+length] - pre_sum[j]
    return result


arr = [1, 4, 2, 5, 3]
print(sumOddLengthSubarrays(arr))

