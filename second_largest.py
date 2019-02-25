
def second_largest(given_array):
    if len(given_array) < 2:
        return None

    largest_order = [None, None]
    if given_array[0] >= given_array[1]:
        largest_order[0] = given_array[0]
        largest_order[1] = given_array[1]
    else:
        largest_order[1] = given_array[0]
        largest_order[0] = given_array[1]

    for i in range(2, len(given_array)):
        if largest_order[0] < given_array[i]:
            largest_order[1] = largest_order[0]
            largest_order[0] = given_array[i]

    return largest_order[1]


a = [1, 3, 4, 0, 2]
print(second_largest(a))
a = [-1, -2]
print(second_largest(a))
a = []
print(second_largest(a))
a = [-1]
print(second_largest(a))
a = [0, -1, 2, 3, 4, 10]
print(second_largest(a))
