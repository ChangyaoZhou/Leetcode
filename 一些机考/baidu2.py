op = [-3, 2]
h = [1, 2, 4, 3]
m = 2
n = 4

stack = []
pid, k = map(int, input().split())
while stack and k >= stack[-1][0]:
    stack.pop()
    if stack and stack[-1][-1] == pid:
        continue
stack.append([k, pid])

for i in range(m):
    if op[i] > 0:
        h = sorted(h[:op[i]]) + h[op[i]:]
    else:
        k = -op[i]
        h = sorted(h[:k], key=lambda x: -x) + h[k:]

for num in h:
    print(num, end='')


