n = 52055545
def count_five(num):
    count = 0
    while num != 0:
        if num % 10 == 5:
            count += 1
        num = num // 10
    return count

#print(count_five(n))
n += 1
while count_five(n) < 5:
    n += 1
print(n)