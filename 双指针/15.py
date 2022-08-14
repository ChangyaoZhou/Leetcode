def threeSum(nums):
    """
    我们要做的是 不能有重复的三元组，但三元组内的元素是可以重复的！
    所以【去重】分为两个步骤
    首先将nums从小到大排序
    1 在遍历nums中的每一项时，如果当前项和前一项相等，则会得到和上一项相同的结果，所以要直接跳过这一次循环
        设当前遍历nums到nums[i],且 nums[i] = nums[i-1]，
        i-1, i, i+1, ...
        — 若nums[i+1:]中存在一对或几对数字，和nums[i-1]组成和为0的三元组，则他们一定全部和遍历nums[i-1]时找到的三元组全部重复
        — 若nums[i+1:]中不存在满足条件的数字，也可以直接continue
    2 确定三元组中的第一个数字后，开始双指针法，当找到一组三元组后，应该如何进行下一步呢?
        为了避免再次找到同样的三元组，不能直接left+=1, right-=1,
        如果有连续几个相同的数字，需要先跳过重复的数字，在进行left+=1, right-=1
        所以此时要和下一个数字比较， 看nums[right] == nums[right - 1]， nums[left] == nums[left + 1]是否满足
        e.g. nums_sorted = [-2, 0, 0, 0, 1, 1, 2, 2, 2] 则会找到三个相同的三元组[-2, 0, 2]
        所以当第一次找到[-2, 0, 2]时, left=1, right=6, 要跳过0右侧的其他0，2左侧的其他2,
        下一个循环时，left=4, right=5, 找到三元组[-2, 1, 1]
    """
    result = []
    nums.sort()
    for i, num in enumerate(nums):
        # 小小的剪枝一下，因为nums按从小到大顺序排序，可以减少一些循环
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left != right and nums[right] == nums[right - 1]:
                    right -= 1
                while left != right and nums[left] == nums[left + 1]:
                    left += 1
                right -= 1
                left += 1

    return result


nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]
nums = [-2,0,0,2,2]
print(threeSum(nums))



