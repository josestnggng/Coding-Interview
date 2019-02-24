def find_pairs(a, k):
    set_a = set(a)
    for x in a:
        if x-k in set_a:
            print(x-k, x)


a = [1, 7, 5, 9, 2, 12, 3]
find_pairs(a, 2)
