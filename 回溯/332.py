def findItinerary(tickets):
    """
    从起点开始搜索backtracking，如果走不下去了，就返回上一层继续搜索，直到找到了字母顺序最小的，可以经过所有城市的路径
    """
    result = ['JFK']
    city_connect = {}
    # 先创建一个dict，又来存放从每个城市出发，分别能到达哪些城市
    for src, dst in tickets:
        if src in city_connect:
            city_connect[src].append(dst)
        else:
            city_connect[src] = [dst]
    print(city_connect)

    def backtracking(tickets, start_pos):
        # backtracking结束的判断条件，有n个tickets，完整的路径就会经过n+1个城市
        if len(result) == len(tickets) + 1:
            return True   # 代表前序的backtracking走到了尽头，找到了符合条件的答案
        if start_pos not in city_connect:  # 如果当前的城市无法通向其他城市，且backtracking还没结束，代表当前路径没法走到头了
            return False
        city_connect[start_pos].sort()  # 因为要字母排序较小的结果，所以先排序
        for i, city in enumerate(city_connect[start_pos]):
            """
            e.g. A:[B, C]当前在城市A，选择走到城市B时，将B删去，变为A:[C]，防止以后再走到A时，还会选择走到城市B，出现死循环
            如果从A走到B再往下走，发现这条路不通，不符合条件，可以再退回到这一层，重新加上B，变回A:[B, C]
            """
            city_connect[start_pos].remove(city)
            result.append(city)
            if backtracking(tickets, city):  # 判断按照当前路径走下去，能不能找到符合条件的答案
                return True
            else:  # 判断按照当前路径走下去，不能找到符合条件的答案，就退回到上一层，继续遍历当前层的其他情况
                result.pop()
                city_connect[start_pos].insert(i, city)

    if backtracking(tickets, 'JFK'):
        return result


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(findItinerary(tickets))
