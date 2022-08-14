
def jump(nums):
    '''
    从后向前搜索，
    第一步，查找能够一步到达终点的点中，位置最靠前，最靠近起点的点（距离终点最远的）
    第二步，将刚才找到的最靠前的点作为终点，继续向前寻找，直到找到起点，记录当前step
    goal = len(nums) - 1
    step = 0
    last_pos = goal
    while goal > 0:
        for i in range(goal - 1, -1, -1):
            if nums[i] >= (goal - i):
                last_pos = min(last_pos, i)
        goal = last_pos
        step += 1
    return step
    '''
    """
    从第一步起，不断更新每一步能够到达的最远范围，如果当前的位置能到达的最远范围不能涵盖目标，就step + 1，
    e.g. nums = [2, 3, 1, 1, 4]
    第一步 curr_distance = 0, 在起点至少还需要一步 step + 1
    接下来遍历从i=0到i=2，更新到达的最远范围             【只走一步最远可以到2】
    第二步 curr_distance = 2,          
          没有到达终点，所以至少还需要一步 step + 1
    接下来遍历从i=2到i=4，更新到达的最远范围为4           【走两步最远可以到4】
    第二步 curr_distance = 4, 到达了终点，直接break
    
    每次的curr distance都是走n步能到达的最远位置
    """
    step = 0
    curr_distance = 0
    next_distance = 0
    for i in range(len(nums)):
        next_distance = max(next_distance, i + nums[i])
        if i == curr_distance:
            if curr_distance != len(nums) - 1:
                step += 1
                curr_distance = next_distance
            else:
                break

    return step



nums = [2, 3, 1, 1, 4]
# nums = [2, 3, 0, 1, 4]
print(jump(nums))
