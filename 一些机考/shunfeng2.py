import math
s = 5
count = 0
for i in range(s, 0, -1):
    count += (i // 2 + 1)
    #print(i // 2 + 1)
#print(count)


def log(n):
    count = 0
    while n > 0:
        n = n >> 1
        #print('n', n)
        count += 1
    return count
count = 0
for i in range(1, s+1):
    count += log(i)
    print(log(i))
print(count)
#print(log(16))
count = 0
for i in range(1, s+1):
    count += (int(math.log2(i)) + 1)
print(count)

m = 0




