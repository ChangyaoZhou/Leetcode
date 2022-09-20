n = 3
k = 15
h = [14, 12, 10]
res = []
start_idx = 0
while start_idx <= n-1:
    for i in range(start_idx, n):
        if abs(max(h[start_idx: i+1]) - min(h[start_idx: i+1])) <= k:
            end_idx = i
        else:
            break
    if (start_idx, end_idx) not in res:
        res.append((start_idx, end_idx))
        start_idx = i
    else:
        break

print(res)









