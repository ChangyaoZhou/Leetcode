def solution(A, M):
    rem_map = {}
    if M == 1:
        return len(A)
    for num in A:
        if num < 0:
            rem = (num % M + M) % M
        else:
            rem = num % M
        if rem in rem_map:
            rem_map[rem] = rem_map[rem] + 1
        else:
            rem_map[rem] = 1
    res = 0
    print(rem_map)
    for rem in rem_map.keys():
        res = max(res, rem_map[rem])
    return res


A = [-3, -2, 1, 0, 8, 7, 1]
M = 3
print(solution(A, M))
