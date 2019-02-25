
def palidrome_permutation(string):
    dict_char = dict()
    no_space_len = 0
    for c in string.lower():
        if c == ' ':
            continue
        if c in dict_char.keys():
            dict_char[c] += 1
        else:
            dict_char[c] = 1
        no_space_len += 1

    max_odd = no_space_len % 2
    count_odd = 0
    for x in dict_char.values():
        if x % 2 == 1:
            count_odd += 1
        if count_odd > max_odd:
            return False

    return True


print(palidrome_permutation("Tact coa"))
print(palidrome_permutation("cdcdcd cdeeeef"))
print(palidrome_permutation("KaRusak Sur"))
