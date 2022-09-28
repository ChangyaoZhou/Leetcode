str1, str2 = ['arc', 'abc']

if str1 == str2:
    found = False
    for i in range(len(str1)):
        if str1.count(str1[i]) >= 2:
            print('Yes')
            found = True
            break
    if not found:
        print('No')
else:
    count = 0
    diff_idx = []
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
            diff_idx.append(i)
    if count != 2:
        print('No')
    elif str1[diff_idx[0]] == str2[diff_idx[1]] and str1[diff_idx[1]] == str2[diff_idx[0]]:
        print('Yes')
    else:
        print('No')

