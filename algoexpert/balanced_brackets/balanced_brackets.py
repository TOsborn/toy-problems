def balancedBrackets(string):
    """Check whether the brackets in a string are balanced."""
    mate = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    openers = set(mate.values())

    stack = []
    for c in string:
        if c in openers:
            stack.append(c)
        elif c in mate:
            if stack == [] or stack.pop() != mate[c]:
                return False

    return stack == []
