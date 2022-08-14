n_seq = [1,2,3,4,5]
n = 5
sum = 0
for n in n_seq:
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