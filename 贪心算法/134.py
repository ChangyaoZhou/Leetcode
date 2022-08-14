def canCompleteCircuit(gas, cost):
    """
    以下两种是暴力解法，会超过时间限制
        for start_idx in range(len(gas)):
        if_start_idx = True
        curr_gas = 0
        gas_new = gas[start_idx:] + gas[:start_idx]
        cost_new = cost[start_idx:] + cost[:start_idx]
        if gas[start_idx] < cost[start_idx]:
            continue
        for i in range(len(gas)):
            curr_gas += gas_new[i]
            curr_gas -= cost_new[i]
            if curr_gas < 0:
                if_start_idx = False
                break
        if if_start_idx:
            return start_idx
    return -1
    """
    """ 
    for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while！
    要模拟跑一圈加油站的过程，用while更合适！！
    for i in range(len(gas)):
        rest = gas[i] - cost[i]
        curr_index = (i + 1) % len(gas)
        while rest >= 0 and curr_index != i:
            rest += (gas[curr_index] - cost[curr_index])
            curr_index = (curr_index + 1) % len(gas)
        if rest >= 0 and curr_index == i:
            return i
    return -1
    """
    # 贪心算法
    # 局部最优：当前累加rest[j]的和curSum一旦小于0，说明rest[i]一定是小于0，因为前序的curr_sum一定是大于0，不然他在前面就被清零了
    # 所以起始位置至少要是j+1，因为从j开始一定不行。

    start = 0
    curSum = 0
    totalSum = 0
    for i in range(len(gas)):
        curSum += gas[i] - cost[i]
        totalSum += gas[i] - cost[i]
        if curSum < 0:
            curSum = 0
            start = i + 1
    if totalSum < 0: return -1
    return start



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))


