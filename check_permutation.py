
def check_permutation(a, b):
    if len(a) != len(b):
        return False

    # sorted a and b, and check if order each element a is same with element of b
    # asume use merge sort : O(nlogn)
    c, d = sorted(a), sorted(b)
    # O(n)
    for i in range(len(c)):
        if c[i] != d[i]:
            return False
    return True
    # O(n) + O(nlogn) = O(nlogn)


print(check_permutation("python", "thopyn"))
print(check_permutation("abc", "abcd"))
print(check_permutation("abc", "abe"))
