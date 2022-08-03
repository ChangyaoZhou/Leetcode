import sys
'''
n = int(sys.stdin.readline().strip())
print(n)
matrix = []
for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        matrix.append(values)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
n = 3
sum = 0
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        sum += abs(matrix[i][j] - matrix[j][i]) * 2
print(sum)


import sys
t = int(sys.stdin.readline().strip())
print(t)
n_seq = []
for _ in range(t):
    n = int(sys.stdin.readline().strip()) 
    sum = 0
    for i in range(1, n + 1):
        sum += i/f_func(i)
'''
n_seq = [1,2,3,4,5]
t = 5



def f_func(n):
    s = n
    binary = []
    count = 0
    while s != 1:
        res = s % 2
        binary.append(res)
        if res == 1:
            return pow(2, count)
        count += 1
        s = int(s / 2)
    return pow(2, count)


print(f_func(33))

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            sum += i
        else:
            while i != 1:
                res = i % 2
                if res == 1:
                    sum += i
                    break
                i = int(i / 2)
            sum += 1
    print(sum)


for n in n_seq:
    sum = 0
    for i in range(1, n + 1):
        sum += i/f_func(i)
    print(sum)


#print(f_func(16))


