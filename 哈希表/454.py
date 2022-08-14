def fourSumCount(nums1, nums2, nums3, nums4):
    """
    【哈希表】经常用来存放各个值出现的次数/频率，或者索引
    首先定义 一个哈希表，key是a和b两数之和的不用结果，value是a和b两数之和出现的次数。
    遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到哈希表中。

    然后遍历大C和大D数组， 对于每一个两数之和sum_34，查找上述哈希表里面是否有-sum_34，如果有，说明对应的四个数加和为0
    累积哈希表中的次数就是最终结果


    """
    sum_ab, sum_cd = {}, {}
    for num1 in nums1:
        for num2 in nums2:
            if num1 + num2 in sum_ab:
                sum_ab[num1 + num2] += 1
            else:
                sum_ab[num1 + num2] = 1
    sum_count = 0
    for num3 in nums3:
        for num4 in nums4:
            sum_34 = num3 + num4
            if -sum_34 in sum_ab:
                sum_count += sum_ab[-sum_34]
    return sum_count


nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(fourSumCount(nums1, nums2, nums3, nums4))

