# a and b in range 0..9 and first character should be 1...9
# can't use string convertion


def largest_string(a, b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b

    # len(a) == len(b)
    for i in range(len(a)):
        if a[i] > b[i]:
            return a
        elif b[i] > a[i]:
            return b

    return None


print(largest_string("202", "203"))
print(largest_string("202", "1203"))
print(largest_string("10", "1"))
print(largest_string("10", "10"))
print(largest_string("11054", "11055"))
