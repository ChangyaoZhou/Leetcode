def find_front_word(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    #print('vocalbulary:', letters)
    # find front word
    if word == 'aaaaaaaaa':
        return None
    else:
        word_list = list(word)
        cur_pos = 8
        while cur_pos >= 0:
            idx = letters.index(word_list[cur_pos])
            if idx - 1 >= 0:
                word_list[cur_pos] = letters[idx - 1]
                break
            else:
                word_list[cur_pos] = letters[-1]
                cur_pos -= 1
        return ''.join(word_list)


def find_back_word(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    # find front word
    if word == 'iiiiiiiii':
        return None
    else:
        word_list = list(word)
        cur_pos = 8
        while cur_pos >= 0:
            idx = letters.index(word_list[cur_pos])
            if idx + 1 <= 8:
                word_list[cur_pos] = letters[idx + 1]
                break
            else:
                word_list[cur_pos] = letters[0]
                cur_pos -= 1
        return ''.join(word_list)


def if_valid(word):
    return set(list(word)) == set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])


word = 'ihgfeadbc'
curr_fword = find_front_word(word)
while not if_valid(curr_fword):
    curr_fword = find_front_word(curr_fword)
print('front word:', curr_fword)

curr_bword = find_back_word(word)
while not if_valid(curr_bword):
    curr_bword = find_back_word(curr_bword)
print('back word:', curr_bword)


#print(find_front_word(word))
#print(find_back_word(word))
