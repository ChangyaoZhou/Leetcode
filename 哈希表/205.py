def isIsomorphic(self, s: str, t: str) -> bool:
    map_s2t, map_t2s = {}, {}
    for i in range(len(s)):
        if s[i] not in map_s2t:
            map_s2t[s[i]] = t[i]

