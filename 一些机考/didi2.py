n = 6
data_list = [[4, 4], [1, 1], [3, 3], [2, 3], [1, 2], [2, 2]]
data_list = [[1, 1],[1, 2], [2, 2], [2, 3],[3, 3],[4, 4]]
#data_sorted = data_list.sorted(key=lambda x:x[0])
#print(data_sorted)

res = []
res_num = 0
path = []


def backtracking(n, k, start_idx, res_num):
    if len(path) == k:
        res_num += 1
        #res.append(path[:])
        return

    tmp = k - len(path)
    for i in range(start_idx, n):
        if path == [] or path[-1][-1] < data_list[i][0]:
            path.append(data_list[i])
            backtracking(n, k, i+1, res_num)
            path.pop()

backtracking(n, 3, 0, res_num)
#print(res)
print(res_num)
