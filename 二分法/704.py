def search(nums, target):
    # 【经典二分法】
    ######## 定义 target 是在一个在左闭右闭的区间里
    left = 0
    right = len(nums) - 1
    while left <= right:
        # 定义target在左闭右闭的区间里，即：[left, right]，left=right时，有意义
        # 随着循环进行，left和right会越来越接近，最后相等，则说明找不到target，循环结束
        middle = (left + right) // 2
        if target < nums[middle]:
            right = middle - 1
            #  right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target,
            #  所以要将right赋值为middle的前一位（比nums[middle]更小的一位）
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle
    return -1


nums = [-1,0,3,5,9,12]
print(search(nums, 8))

"""
step    left    mid     right       compare
0       0       2       5           tar>nums[mid]
1       3       4       5           tar<nums[mid]
2       3       3       3           tar>nums[mid]
3       4               3    -->结束循环 
"""

