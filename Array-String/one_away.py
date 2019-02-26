
def one_away(first, second):
    if abs(len(first)-len(second) > 1):
        return False

    # first < second
    if len(first) > len(second):
        first, second = second, first

    i, j = 0, 0
    found_diff = False
    while i < len(first) and j < len(second):
        if first[i] != second[j]:
            if found_diff:
                return False
            found_diff = True
            if len(first) == len(second):
                i += 1
            j += 1
        else:
            j += 1
            i += 1

    return True


print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pales", "paxes"))
print(one_away("pale", "bale"))
print(one_away("pale", "bae"))
