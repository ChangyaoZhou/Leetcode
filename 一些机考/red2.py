height = [1, 5, 3, 4, 2]
n = 6
k = 2
curr_pos = 0
cost = 0
'''
while curr_pos < n-1:
    min_height = max(height)
    min_i = 0
    for i in range(1, k+1):
        if curr_pos + i > n-1:
            break
        if height[curr_pos + i] <= min_height:
            min_i = i
            min_height = height[curr_pos + i]
    if height[curr_pos + min_i] > height[curr_pos]:
        cost += height[curr_pos + min_i] - height[curr_pos]
    curr_pos += min_i
print(cost)
'''
dp = [0, min(0, height[1] - height[0])]
#for i in range(2, n-1):
    #if height[i] <= height[i-1]:







