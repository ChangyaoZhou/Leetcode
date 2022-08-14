'''
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: -x[0])
    count = 1
    end = intervals[0][0]
    for i in range(1, len(intervals)):
        if end >= intervals[i][1]:
            count += 1
            end = intervals[i][0]
    return len(intervals) - count
'''

def eraseOverlapIntervals(intervals):
    """
    这道题和452题原理一模一样，其实都在求给的区间里面最多有几个互相不重叠的区间
    452中，有几个互相不重叠的区间，就需要射几箭
    本题中，一共有n个区间，其中有m个互相不重叠的区间，则需要去掉(n-m)个区间，才可以满足条件
    互相不重叠的区间e.g. [2,4], [5,6], [7,9]

    如何求最多有几个互相不重叠的区间呢？
    首先，判断两个区间是否重叠，可以比较A的右边界和B的左边界，所以我们可以先将所有区间按照右边界从小到大排序，然后从小到大来遍历，
    end表示的是当前和前面不重叠的区间的右边界，如果下一个区间的左边界 > end, 则我们发现了下一个和前面不重叠的区间，就需要更新end的值
    e.g. intervals = [[10,16],[2,8],[1,6],[7,12]]
         intervals_sorted = [[1,6], [2,8], [7,12], [10,16]]
    end初始化为排序后第一个区间的右边界，即最小的右边界
    step    end     当前interval      是否是一个新的不重叠区间        count
    0       6           /                   /                     1
    1       6         [2, 8]                false                 1
    2       6         [7, 12]               7>6, true             2
    3       12        [10, 16]              false                 2      -->一共有两个不重叠区间

    P.S.同理，也可以首先将所有区间按照左边界从大到小排列，再按照左边界从大到小的顺序遍历所有区间，是一样的！！！见上面代码
    """

    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if end <= intervals[i][0]:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count


intervals = [[10,16],[2,8],[1,6],[7,12]]
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
