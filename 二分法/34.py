def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle
    return -1


def searchRange(nums, target):
    """
    给你一个按照非递减顺序排列的整数数组nums，和一个目标值target。请你找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值target，返回[-1, -1]。

    // 解法2
    // 1、首先，在 nums 数组中二分查找 target；
    // 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
    // 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间

    """
    idx = binary_search(nums, target)
    if idx == -1:
        return [-1, -1]
    else:
        for left in range(idx, -1, -1):
            if nums[left] != target:
                left += 1
                break
        for right in range(idx, len(nums)):
            if nums[right] != target:
                right -= 1
                break
        return [left, right]


nums = [5, 7, 7, 8, 8, 10]
nums = [1]
target = 1
print(searchRange(nums, target))

