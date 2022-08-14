def findMinArrowShots(points):
    """
    贪心算法：当气球出现重叠，一起射，所用弓箭最少
    先将所有气球按起始位置从小到大排序，然后从前往后遍历，看有没有和前面的气球重合
    """
    points.sort(key=lambda x: x[0])
    arrow = 1
    right_border = points[0][1]
    # right_border表示当前这一箭射到(几个重合的)气球的最右侧边界，用来判断后面的气球有没有和前面的重合首先设为第一个气球的右边界
    # e.g. 排序后 points = [[1,6],[2,8],[7,12],[10,16]]
    # 很明显，前两个气球重合，right border = 6, 第三个气球的起点要小于6，才能和前两个气球有重合部分
    for i in range(1, len(points)):
        if points[i][0] <= right_border:
            right_border = min(right_border, points[i][1])
        else:
            arrow += 1
            right_border = points[i][1]
            # 若判断当前气球不和前面的重合，则将当前的气球右边界设为新的right border
    return arrow


points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))
