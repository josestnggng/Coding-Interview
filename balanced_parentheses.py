
def is_balance(string):
    stack = []
    tokens = {"}": "{", "]": "[", ")": "("}

    for x in string:
        if x in tokens.values():
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            start = stack.pop()
            start_expected = tokens[x]
            if start != start_expected:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_balance("({})[()]"))
    print(is_balance(")()"))
    print(is_balance("([]"))
