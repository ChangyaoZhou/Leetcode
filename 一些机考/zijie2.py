from collections import Counter
s = 'ASAFASAFADDD'
cnt = Counter(s)
res = len(s)
i = 0
avr = len(s) // 4
for j, c in enumerate(s):
    cnt[c] -= 1
    while i < len(s) and all(avr >= cnt[x] for x in 'ASDF'):
        res = min(res, j - i + 1)
        cnt[s[i]] += 1
        i += 1
print(res)


