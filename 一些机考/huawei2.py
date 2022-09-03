command = 'SM0SF0'
command = 'S{{M0S}F0}F0'
def count_error(command):
    num_m = command.count('M')
    num_f = command.count('F')
    if num_m >= num_f:
        explode = num_m - num_f
    else:
        explode = 0
    error = max(num_f - num_m, 0)
    output = str(num_m) + ',' + str(num_f) + ',' + str(explode) + ',' + str(error)
    print(output)
    #print num_m, num_f, explode, error

#count_error(command)

def count_error2(command):
    all_level = command.count('{') + 1
    level = 0
    m_count = [0 for _ in range(all_level)]
    f_count = [0 for _ in range(all_level)]
    for i in range(len(command)):
        if command[i] == '{':
            level += 1
        if command[i] == '}':
            level -= 1
        if command[i] == 'M':
            m_count[level] += 1
        if command[i] == 'F':
            f_count[level] += 1
    num_m = sum(m_count)
    num_f = sum(f_count)
    if num_m > num_f:
        explode = num_m - num_f
    else:
        explode = 0
    # explode = 0
    error = 0
    for i in range(len(m_count)):
        #if m_count[i] > f_count[i]:
            # explode += (m_count[i] - f_count[i])
        if f_count[i] > m_count[i]:
            error += (f_count[i] - m_count[i])
    output = str(num_m) + ',' + str(num_f) + ',' + str(explode) + ',' + str(error)
    print(output)


count_error2(command)
