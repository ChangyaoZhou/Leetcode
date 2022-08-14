def twoSum(nums, target):
    """
    用一个哈希表来储存nums，key是nums中每一个元素的值，value是nums中每一个元素的索引
    对于nums中每一个元素，查找res=target - num是否已经存在在hash table里面
    """
    hash_table = {}
    for i, num in enumerate(nums):
        # 查找target - num是否在hash table中，即查找target - num是否在hash table的key中，如果没有就把当前值存下来
        if target - num not in hash_table:
            hash_table[num] = i
        else:
            return [i, hash_table[target - num]]


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
