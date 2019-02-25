
def palidrome_permutation(string):
    dict_char = dict()
    no_space_len = 0
    for c in string.lower():
        if c == ' ':
            continue
        if c in dict_char.keys():
            dict_char[c] = 0
        else:
            dict_char[c] = 1
        no_space_len += 1

    if no_space_len % 2 != sum(dict_char.values()):
        return False
    return True


print(palidrome_permutation("Tact coa"))
print(palidrome_permutation("cdcdcd cdeeeef"))
print(palidrome_permutation("KaRusak Sur"))
