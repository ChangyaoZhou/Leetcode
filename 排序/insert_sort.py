"""
1、从数组第2个元素开始抽取元素。
2、把它与左边第一个元素比较，如果左边第一个元素比它大，则继续与左边第二个元素比较下去，直到遇到不比它大的元素，然后插到这个元素的右边。
3、继续选取第3，4，....n个元素,重复步骤 2 ，选择适当的位置插入。

性质：1、时间复杂度：O(n2) 2、空间复杂度：O(1) 3、稳定排序 4、原地排序
"""

def insert_sort(nums):
    for i in range(1, len(nums)):  # 取出第i个元素，把它的值先放入tmp中
        tmp = nums[i]
        k = i - 1  # 从i的前一位开始比较，拿nums[i]和前面的每一位比较，直到k<0或找到一个比nums[i]小的数
        while k >= 0 and tmp < nums[k]:
            k -= 1
        # 此时k是从右往左，第一个小于nums[i]的数的索引
        # 要从i减小到k+1，每一位都向右移动一位
        for j in range(i, k+1, -1):
            nums[j] = nums[j-1]
        # 最后将第k+1位存入tmp
        nums[k+1] = tmp
    print(nums)


nums = [9, 2, 4, 6, 7, 3, 1, 5, 8, 0, 2, 3]
insert_sort(nums)
