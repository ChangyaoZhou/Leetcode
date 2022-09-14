def bubble_sort_better(nums):
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


def nextPermutation(nums):
    """
    实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。


    1 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。
    比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
    2 我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。
    e.g. 1243
    - 所以需要从低位开始，从后向前遍历，找到一组后面的「大数」与前面的「小数」， 后面的大数尽量低位，前面的小数也尽量低位
    当nums[j] > nums[i]时, 交换 后面的「大数」与前面的「小数」。
    - 将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
    """
    l = len(nums)
    for i in range(l-1, -1, -1):
        for j in range(l-1, i, -1):
            if nums[j] > nums[i]:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                sub_list = nums[i+1:]
                bubble_sort_better(sub_list)
                nums[i + 1:] = sub_list
                return
    nums.reverse()


nums = [1, 2, 4, 3]
nums = [1, 1, 5]
nums = [2, 3, 1]
nextPermutation(nums)
print(nums)

