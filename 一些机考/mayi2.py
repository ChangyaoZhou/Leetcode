num = 16
dp = [0 for _ in range(num)]


def if_zhishu(num):
    if num == 2:
        return True
    else:
        i = 2
        while i < num:
            if num % i == 0:
                return False
            i += 1
        return True


def find_closest_zhishu(num):
    while num > 1:
        if if_zhishu(num):
            return num
        num -= 1

def find_num_zhishu(num):
    count = 0
    while num > 1:
        for i in range(2, num+1):
            if num % i == 0 and if_zhishu(i):
                count += 1
                break
        num = num // i
    return count

#print(find_num_zhishu(16))
#print(find_closest_zhishu(16))



for i in range(2, num+1):
    if if_zhishu(i):
        dp[i-1] = 1
    else:
        idx = find_closest_zhishu(i)
        for pos in range(idx, i):
            dp[i-1] = min(dp[i-1], dp[pos] + i - pos)
        num_zhishu = find_num_zhishu(i)
        dp[i-1] = min(dp[i-1], num_zhishu)
print(dp)
print(dp[-1])

