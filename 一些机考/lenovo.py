n = 5
m = 2
input_str = ['A', 'B', 'B', 'A', 'B']

def find_first_a(ab_list):
    for i in range(len(ab_list)):
        if ab_list[i] == 'A':
            return i
'''
#num_a = input_str.count('A')
op_count = 0
for i in range(len(input_str)):
    if input_str[i] == 'B':
        if find_first_a(input_str[i+1:]):
            a_idx = find_first_a(input_str[i+1:]) + i + 1
            input_str[i] = 'A'
            input_str[a_idx] = 'B'
            op_count += 1

num_a = input_str.count('A')
if m > op_count:
    input_str[num_a: num_a + m - op_count]
'''
op_count = 0
i = 0
while op_count < m:
    if input_str[i] == 'B':
        input_str[i] = 'A'
        op_count += 1
    if i > n - 1:
        break
    i += 1
'''
if m > op_count:
    for i in range(len(input_str)):
        if input_str[i] == 'B':
            if find_first_a(input_str[i + 1:]):
                a_idx = find_first_a(input_str[i + 1:]) + i + 1
                input_str[i] = 'A'
                input_str[a_idx] = 'B'
                op_count += 1
'''
print(''.join(input_str))

