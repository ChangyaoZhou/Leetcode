def twoSum(numbers, target):
    """
    数组numbers已按非递减顺序排列
    使用两个指针，分别从头尾开始找，
    1 如果两个指针指向元素的和 sum == target，那么得到要求的结果；
    2 如果 sum > target，移动较大的元素，使 sum 变小一些；
    3 如果 sum < target，移动较小的元素，使 sum 变大一些。
    """
    i = 0
    j = len(numbers) - 1
    while (True):
        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
