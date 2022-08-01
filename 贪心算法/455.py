def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    i = len(g) - 1
    count = 0
    for j in range(len(s) - 1, -1, -1):
        while s[j] < g[i]:
            i -= 1
        i -= 1
        count += 1
    return count

g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))
