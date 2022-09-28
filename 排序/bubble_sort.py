"""
1、把第一个元素与第二个元素比较，如果第一个比第二个大，则交换他们的位置。接着继续比较第二个与第三个元素，如果第二个比第三个大，则交换他们的位置....
***我们对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样一趟比较交换下来之后，排在最右的元素就会是最大的数。
除去最右的元素，我们对剩余的元素做同样的工作，如此重复下去，直到排序完成。

性质：1、时间复杂度：O(n2) 2、空间复杂度：O(1) 3、稳定排序 4、原地排序
"""


def bubble_sort(nums):
    for i in range(0, len(nums)-1):  # 每次循环之后都会在末尾固定一个当前活动数组中的最大值
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    print(nums)
     


def bubble_sort_better(nums):
    """
    优化一下冒泡排序的算法
    假如从开始的第一对到结尾的最后一对，相邻的元素之间都没有发生交换的操作，
    这意味着右边的元素总是大于等于左边的元素，此时的数组已经是有序的了，我们无需再对剩余的元素重复比较下去了。
    """
    for i in range(0, len(nums)-1):  # 每次循环之后都会在末尾固定一个当前活动数组中的最大值
        change = False
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                change = True
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
        if not change:
            break
    print(nums)


nums = [9, 2, 4, 6, 7, 3, 1, 5, 8, 0, 2, 3]
bubble_sort_better(nums)


