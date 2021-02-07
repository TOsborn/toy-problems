def runLengthEncoding(string):
    """Return the run-length encoding of a string.

    >>> ""
    ''
    >>> runLengthEncoding("A")
    '1A'
    >>> runLengthEncoding("AAA")
    '3A'
    >>> runLengthEncoding("AAAAAAAAAAAA")
    '9A3A'
    >>> runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
    '9A4A2B4C2D'
    """
    rle = ""
    i = 0
    while i < len(string):
        cnt = 1
        while cnt < 9 and i+1 < len(string) and string[i+1] == string[i]:
            cnt += 1
            i += 1

        rle += f"{cnt}{string[i]}"
        i += 1

    return rle


if __name__ == "__main__":
    import doctest
    doctest.testmod()
