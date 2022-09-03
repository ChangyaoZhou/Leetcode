"""
首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置(如果第一个元素就是最小元素那么它就和自己交换)。
其次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。
如此往复，直到将整个数组排序。这种方法我们称之为选择排序。

性质：1、时间复杂度：O(n2) 2、空间复杂度：O(1) 3、非稳定排序 4、原地排序
"""
def select_sort(nums):
    for i in range(len(nums)):
        min_num = nums[i]
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < min_num:
                min_num = nums[j]
                min_idx = j

        tmp = nums[i]
        nums[i] = min_num
        nums[min_idx] = tmp
    print(nums)


nums = [9, 2, 4, 6, 7, 3, 1, 5, 8, 0, 2, 3]
select_sort(nums)
