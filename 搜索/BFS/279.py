def numSquares(n):
    """
    给你一个整数 n ，返回和为 n的完全平方数的最少数量，n可以最少由几个完全平方数组成
    因为要求的是个数最少的完全平方数，所以可以用广度优先搜索 BFS
    从上到下进行遍历，在每一层时，都要遍历当前层的所有节点，然后再进行下一层

    注意！！！本题如果用list就会超时，如果用set，运行时间会少很多！！！
    list.append要尽量少做，set.add在运行时间上要快很多！！！
    set也可以保留顺序
    """
    square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
    queue = {n}  # 用于存放接下来待访问的节点
    visited = {n}  # 用于存放访问过的节点
    step = 0
    while queue:
        step += 1
        new_queue = set()
        for cur_n in queue:
            # cur_n = queue.pop(0)
            for sq_num in square_nums:
                # 将每一层的数减去完全平方数的剩余部分，当作下一层的节点值
                res = cur_n - sq_num
                if res == 0:
                    return step
                elif res < 0:
                    break
                elif res not in visited:
                    # 如果没有访问过当前节点，就把当前节点放入queue中，
                    new_queue.add(res)
                    visited.add(res)
        queue = new_queue
    return -1


print(numSquares(12))



