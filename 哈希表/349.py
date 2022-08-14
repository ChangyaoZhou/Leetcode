def intersection(nums1, nums2):
    # return list(set(nums1) & set(nums2))  # 求set1和set2的交集#
    return list(set(nums1).intersection(set(nums2)))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
"""
set()可以用来去掉list中的重复项
e.g. list1 = [1,1,1,3,4,5,5,5]  --> set(list1) = {1,3,4,5}



python set之间的各种运算
e.g. set1={1,2,3}  set2={3,4,5}
运算操作	Python运算符	    含义	                            例子                结果
交集	        &	        取两集合公共的元素	                >>> set1 & set2    {3}
并集	        |	        取两集合全部的元素	                >>> set1 | set2    {1,2,3,4,5}
差集	        -	        取一个集合中另一集合没有的元素	    >>> set1 - set2    {1,2} 
对称差集	    ^	        取集合 A 和 B 中不属于 A&B 的元素	>>> set1 ^ set2    {1,2,4,5}
"""
