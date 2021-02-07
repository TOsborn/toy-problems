def minimumWaitingTime(queries):
    """Return the minimum waiting time across all queries.

    >>> minimumWaitingTime([10])
    0
    >>> minimumWaitingTime([5, 1])
    1
    >>> minimumWaitingTime([3, 2, 1, 2, 6])
    17
    >>> minimumWaitingTime([])
    0
    """
    n = len(queries)
    return sum(((n - i - 1))*q for i, q in enumerate(sorted(queries)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
