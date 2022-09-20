n1 = 3
nums1 = [1, 2, 3]
n2 = 4
nums2 = [4, 5, 6, 7]
matrix = [[0 for _ in range(n2)] for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        matrix[i][j] = nums1[i] * nums2[j]
result1 = []

for n in range(n1 + n2 - 1):
    yn = 0
    for i in range(n):
        if i > n1-1:
            break
        j = n-i
        yn += matrix[i][j]
    result1.append(yn)

print(result1)

