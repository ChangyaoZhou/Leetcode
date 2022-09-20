pos = [[100, 280], [190, 360], [150, 360]]
pos = [[0, 1000, 2000, 3010, 3200], [40, 1050, 2049, 3100], [80], [120], [160]]
n = 5
count = len(pos[0])


def check(curr_layer, last_layer):
    for pos in curr_layer:
        if_keep = False
        for i in range(0, len(last_layer)):
            if i != len(last_layer)-1 and abs(pos - last_layer[i]) < 50:
                if_keep = True
                break
            elif i != len(last_layer)-1 and pos < last_layer[i] + 100 and pos + 100 > last_layer[i+1]:
                if_keep = True
                break
            elif i == len(last_layer)-1 and abs(pos - last_layer[-1]) < 50:
                if_keep = True
                break
        if not if_keep:
            curr_layer.remove(pos)
    return curr_layer




for i in range(1, n):
    curr_layer = check(pos[i], pos[i-1])
    pos[i] = curr_layer
    count += len(curr_layer)

print(count)

