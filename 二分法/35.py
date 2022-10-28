def searchInsert(nums, target):
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
    e.g. nums = [1,3,5,6], target = 2
    插入后nums = [1,2,3,5,6], 插入后2的索引是1，所以返回1

    【法一】 二分法
    前面和704题一样，正常的二分法，如果target在nums中，返回其索引
    如果target不在nums中，就要找出他插入nums后的索引
    ***不管二分法前面怎么循环，都是由left>right跳出循环的，他的前一步一定是left=right=middle
    ***在二分法中，每一次循环时，对于left，right，都一定有target > nums[left - 1], target < nums[right + 1]

    因此，在跳出循环的倒数第二步，left=right=middle=i时，有两种情况：
    【1】 target > nums[i], 则 l=mid+1=i+1, r=i, (l>r,会跳出循环)
        但已知 target < nums[i + 1], 所以target会插在nums[i], nums[i+1]中间，插入后的索引为r+1=i+1
    【2】 target < nums[i], 则 r=mid-1=i-1, l=i, (l>r,会跳出循环)
        但已知 target > nums[i - 1], 所以target会插在nums[i-1], nums[i]中间，插入后的索引为r+1=i
    综上，如果target不在nums中，他插入nums后的索引一定是right+1!!!!
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return right + 1
    """
    法二：暴力解法
    
    for i in range(len(nums)):
        # 如果target比其中第i个数小，则要插在第i个数前面，插入后的索引为i
        if target <= nums[i]:
            return i
    # 如果target是最大的，或者 nums为空，则返回nums的长度
    return len(nums)
    """

nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))

