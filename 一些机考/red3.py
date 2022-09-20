nums = [1, 2, 1, 3, 2, 3]
n = 6
k = 2

def check(nums, k):
    numset = set(nums)
    for num in numset:
        if nums.count(num) >= k:
            return True
count = 0
#res = []
for i in range(0, n-k+1):
    for j in range(i+k, n+1):
        if check(nums[i: j], k):
            #res.append(nums[i: j])
            count += n - j + 1
            break
print(count)
#print(res)
