nums = [232, 233, 466, 23300]
num = 23300
t = len(str(num)) - 3

count = 0
found = False
while t >= 0:
    if num - pow(10, t) * 233 < 0:
        t -= 1
    elif num - pow(10, t) * 233 > 0:
        num = num - pow(10, t) * 233
        count += 1
    elif num - pow(10, t) * 233 == 0:
        count += 1
        print(count)
        found = True
        break
if not found:
    print(-1)
