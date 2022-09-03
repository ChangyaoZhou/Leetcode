cost = [[0.9, 0.8, 0.8, 0.1],
        [0.5, 0.4, 0.3, 0.8],
        [0.2, 0.1, 0.4, 0.8],
        [0.1, 0.2, 0.5, 0.9]]

def hungarian(cost):
    n = len(cost)
    result = []
    path = []
    min_cost = 2
    min_idx = 0

    def backtracking(cost, start_idx):
        if len(path) == n:
            result.append(path.copy())
            return

        for i in range(start_idx, len(cost)):
            path.append(i)
            backtracking(cost, i+1)
            path.pop()

    backtracking(cost, 0)
    print(result)
    for i, res in enumerate(result):
        cost = sum([cost[i][res[i]] for i in range(len(cost[0]))])
        if cost < min_cost:
            min_cost = cost
            min_idx = i
    return result[min_idx], min_cost


print(hungarian(cost))

