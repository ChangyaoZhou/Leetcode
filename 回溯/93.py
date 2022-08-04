def if_valid_ip(s, start_idx, end_idx):
    '''
    判断ip地址中的每一段是否有效
    段位以0为开头的数字，且不是0的不合法 e.g. 1.128.035.27不合法
    段位如果不在0到255之间不合法
    '''
    if s[start_idx] == '0' and start_idx != end_idx:
        return False
    if not 0 <= int(s[start_idx: end_idx + 1]) <= 255:
        return False
    return True



def restoreIpAddresses(s):
    '''
    本题类似131分割问题，但是分割后的长度是固定的4且分割结果必须是有效的ip地址
    '''
    if len(s) < 4:
        return []
    result = []
    path = []

    def backtracking(s, start_idx):
        tmp = 4 - len(path)
        if len(path) == 4 and start_idx == len(s):
            # 判断当前的分割结束了，且保证是有效的ip， 将path存入result
            result.append(path.copy())
            return
        elif len(s) - start_idx > 3 * tmp:
            # 判断如果后面剩下s没分割的部分太长了，说明前面分割的太少了，没必要再继续遍历了,提前结束
            # e.g. s = "25525511135", path = ['2', '5', '5'] s后面剩下的部分太长了，不可能组成有效的ip
            return

        for i in range(start_idx, len(s)):
            if if_valid_ip(s, start_idx, i):  # 判断是否为有效的ip地址
                path.append(s[start_idx: i + 1])
                backtracking(s, i+1)
                path.pop()

    backtracking(s, 0)
    result_ip = ['.'.join(res) for res in result]  # 合并字符串，把path列表转化成ip地址
    return result_ip


s = "25525511135"
s = '101023'
print(restoreIpAddresses(s))

