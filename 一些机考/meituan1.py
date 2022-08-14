n = 6
t = 5
times = [5,6,7,8,9,10]
times = [100, 101, 102, 103, 104, 105]

times.sort()
magic = 0
curr_time = 0
for i in range(n):
    curr_time += t
    if curr_time > times[i]:
        magic += 1
        curr_time -= t
print(magic)


