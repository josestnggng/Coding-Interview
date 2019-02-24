from math import pow
res = {}
for a in range(10):
    for b in range(10):
        r = pow(a, 3) + pow(b, 3)
        res[r] = [a, b]
for c in range(10):
    for d in range(10):
        r = pow(c, 3)+pow(d, 3)
        ab = res[r]
        print("a^3+ b^3 = {}, c^3+ d^3 = {}".format(
            pow(ab[0], 3)+pow(ab[1], 3), r
        ))
