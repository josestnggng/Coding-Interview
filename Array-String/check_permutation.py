
def check_permutation(a, b):
    if len(a) != len(b):
        return False

    # Asume 128 ASCII
    char_set = [0]*128
    # count
    for x in a:
        char_set[ord(x)] += 1
    for x in b:
        char_set[ord(x)] -= 1
        if char_set[ord(x)] < 0:
            return False

    return True
    # O(n) + O(n) = O(n)


print(check_permutation("python", "thopyn"))
print(check_permutation("abc", "abcd"))
print(check_permutation("abc", "abe"))
