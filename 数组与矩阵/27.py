def removeElement(nums, val):
    length = len(nums)
    i = 0
    while i < length:
        if nums[i] == val:
            for j in range(i+1, length):
                nums[j - 1] = nums[j]
            # 因为后面的元素都向前移动了一位，所以需要考虑的总长度需要-1，
            # 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
            length -= 1
            i -= 1
        i += 1
    # 每发现一次
    return length


nums = [0, 1, 2, 2, 3, 0, 4, 2]
# nums = [3, 2, 2, 3]
val = 2
length = removeElement(nums, val)
print(length)
print(nums)

