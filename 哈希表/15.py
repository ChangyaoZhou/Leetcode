def threeSum(nums):
    """
    本题第一眼看上去，可能类似454题，可以用哈希表，但是因为三个数都要在一个数组里面取，不能重复取，但是数组中可能有重复的项，
    如果用哈希表，结果中会有很多重复，所以本题不适合用哈希表！！！会很麻烦！！！
    """
    hash_table = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] not in hash_table:
                hash_table[nums[i] + nums[j]] = [(i, j)]
            else:
                hash_table[nums[i] + nums[j]].append((i, j))

    result = []
    for i, num in enumerate(nums):
        if -num in hash_table:
            for pair in hash_table[-num]:
                # print(num, set([num, pair[0], pair[1]]))
                if i not in pair:
                    result.append([num, nums[pair[0]], nums[pair[1]]])
    return result

# ***以上方法并没有解决重复三元组的问题


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))




