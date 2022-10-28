def contain_t(window_map, t):
    for str in set(t):
        if list(t).count(str) > window_map[str]:
            return False
    return True


def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    from collections import defaultdict
    min_res = len(s)+1
    min_i = -1
    min_j = -1
    window_map = defaultdict(int)
    j = 0
    for i in range(len(s) - len(t)+1):
        if i > 0:
            window_map[s[i-1]] -= 1
        while j <= len(s):
            if contain_t(window_map, t):
                if j - i < min_res:
                    min_res = j - i
                    min_i = i
                    min_j = j
                    print(min_res, min_i, min_j)
                break
            if j != len(s):
                window_map[s[j]] += 1
            j += 1


    if min_res == len(s) + 1:
        return ""
    else:
        return s[min_i: min_j]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))



