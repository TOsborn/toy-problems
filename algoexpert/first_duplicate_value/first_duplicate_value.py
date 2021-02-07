def firstDuplicateValue(array):
    """Return the first duplicate element.

    Uses constant additional memory at the cost of mutating the input array.
    """
    array.reverse()
    appeared = set()
    while array:
        a = array.pop()
        if a in appeared:
            return a

        appeared.add(a)

    return -1

def unoptimized_firstDuplicateValue(array):
    """Return the first duplicate element."""
    appeared = set()
    for a in array:
        if a in appeared:
            return a

        appeared.add(a)

    return -1
