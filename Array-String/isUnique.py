"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def isUnique(string):
    # Asume 128 ASCII
    if len(string) > 128:
        return False

    char_set = [False]*128
    for i in range(len(string)):
        char_in_int = ord(string[i])
        if char_set[char_in_int]:
            return False
        char_set[char_in_int] = True

    return True


print(isUnique("abcd"))
print(isUnique("abcda"))
