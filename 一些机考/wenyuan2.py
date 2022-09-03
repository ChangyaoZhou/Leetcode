n, m, k = 3, 3, 4

from collections import deque
k_max = deque([])
F = []
for i in range(m, 0, -1):
    for j in range(n, 0, -1):
        if len(F) < k:
            F.append(i * j)
            if len(F) == k:
                F.sort(reverse=True)
            '''
            for idx in range(len(F)-1, 0, -1):
                if F[idx] > F[idx - 1]:
                    tmp = F[idx]
                    F[idx] = F[idx - 1]
                    F[idx - 1] = tmp 
            '''

        elif len(F) == k:
            if i * j > F[-1]:
                F[-1] = i * j
                for idx in range(k-1, 0, -1):
                    if F[idx] > F[idx-1]:
                        tmp = F[idx]
                        F[idx] = F[idx-1]
                        F[idx-1] = tmp
            else:
                break
#print(F)
print(F[-1])

'''
num = k // 3
num2 = k % 3
i = m - num
j = n - num
if num2 == 0:
    print(min(i*(j+1), j*(i+1)))
if num2 == 1:
    print(i * j)
if num2 == 2:
    print(max(i*(j-1), j*(i-1)))
'''










