time1 = [1, 3, 2, 9, 1]
time2 = [4, 6, 1]
n = 3
m = 5
t = 15

time1_sum = []
for i in range(len(time1)):
    t_sum = sum(time1[:i+1])
    if t_sum <= t:
        time1_sum.append(t_sum)
        index1 = i
    else:
        break

time2_sum = []
for i in range(len(time2)):
    t_sum = sum(time2[:i+1])
    if t_sum <= t:
        time2_sum.append(t_sum)
        index2 = i
    else:
        break

#time1_sum = [sum(time1[:i+1])for i in range(len(time1))]
#time2_sum = [sum(time2[:i+1])for i in range(len(time2))]
#print(time1_sum, index1)
#print(time2_sum, index2)

'''
for i in range(len(time1_sum)):
    if time1_sum[i] < t:
        t_rest = t - time1_sum[i]
        for j in range(len(time2_sum)-1, -1, -1):
            if t_rest 
'''
result = 0
for i in range(index1, -1, -1):
    for j in range(index2, -1, -1):
        if time1_sum[i] + time2_sum[j] <= t:
            result = max(result, i+j)
            break
print(result+2)


