def candy(ratings):
    """
    本题没法同时考虑两边，所以要把相邻拆分成左边和右边
    先给所有人初始赋值为1，然后先从左向右遍历，再从右向左遍历，
    从左向右遍历: 只考虑右边的人比左边的人评分高的情况：对于每一个孩子，如果当前孩子评分大于他左边的孩子，就给当前孩子糖果在左侧人基础上+1
    然后从右向左遍历，只考虑左边的人比右边的人评分高的情况: 对于每一个孩子，如果当前孩子评分大于他左边的孩子，就给当前孩子糖果在右侧人基础上+1
    """
    candys = [1 for i in range(len(ratings))]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candys[i] = candys[i-1] + 1
    for j in range(len(ratings)-2, -1, -1):
        if ratings[j] > ratings[j+1] and candys[j] <= candys[j+1]:
            candys[j] = candys[j+1] + 1
    return sum(candys)


ratings = [1,0,2]
ratings = [1,3,2,2,1]
ratings = [1,2,87,87,87,2,1]
print(candy(ratings))

