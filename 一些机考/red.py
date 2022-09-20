scores = [[4], [7, 7, 1, 1, 6, 9], [6, 6], [8]]
a1, a2, a3, a4 = 1, 2, 2, 1
x = 2
'''
if_valid = True
while num < num_max:
    for i in range(4):
        valid = False
        for j in range(a_nums[i]):
            if scores[i][j] > x:
                scores[i].pop(j)
                valid = True
                break
        if not valid:
            print(0)
            break

    if valid:
        num += 1
    else:
        break
'''
nums = []
for scr in scores:
    num = 0
    for s in scr:
        if s > x:
            num += 1
    nums.append(num)
#print(nums)
print(min(nums))




