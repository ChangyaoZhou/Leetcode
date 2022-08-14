n = 4
nums = [1, 2, 3, 4]
'''
origin = []
origin.append(str(nums[-1]))
origin.insert(0, str(nums[-2])) 

for i in range(-3, -len(nums) - 1, -1):
    origin = [str(nums[i])] + origin
    origin = origin[-2:] + origin[:-2]


print(''.join(origin))
'''
from collections import deque
origin = deque([str(nums[-2]), str(nums[-1])])

for i in range(-3, -len(nums) - 1, -1):
    origin.appendleft(str(nums[i]))
    origin.appendleft(origin.pop())
    origin.appendleft(origin.pop())
#print(origin)
print(''.join(origin))




