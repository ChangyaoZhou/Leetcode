def solution(A, B):
    # write your code in Python (Python 3.6)
    C = []

    for i in range(len(A)):
        C.append(max(A[i], B[i]))
    for i in range(1, 100001):
        if i not in C:
            return i


def if_m_align(nums, M):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] - nums[j]) % M != 0:
                return False
    return True


def solution(A, M):
    # write your code in Python (Python 3.6)

    if M == 1:
        return len(if_m_align)
    result = []
    path = []
    A.sort()

    def backtracking(A, start_idx):
        if start_idx == len(A):
            return

        for i in range(start_idx, len(A)):
            if i > start_idx and A[i] == A[i - 1]:
                continue
            path.append(A[i])
            result.append(path[:])
            backtracking(A, i + 1)
            path.pop()

    backtracking(A, 0)
    max_len = len(A)
    for max_len in range(len(A), 2, -1):
        for res in result:
            if len(res) == max_len and if_m_align(res, M):
                return max_len
    return 1


def solution(S):
    # write your code in Python (Python 3.6)
    for i in range(len(S), 0, -1):
        for j in range(0, len(S) - i + 1):
            sub = S[j: j + i]
            # print(sub)
            has_odd = False
            for l in range(26):
                if sub.count(chr(ord('a') + l)) % 2 != 0:
                    has_odd = True
                    break
            if not has_odd:
                return i
    return 0