def powerset(array):
    """Return the powerset of an array as a list of lists."""
    ps = [[]]
    for a in array:
        for i in range(len(ps)):
            ps.append(ps[i]+[a])
        
    return ps

###################################

def powerset2(array):
    """Return the powerset of an array as a list of lists."""
    return list(_powersetIterator(array))

def _powersetIterator(array):
    n = len(array)
    for i in range(2**n):
        yield [array[j] for j in range(n) if 2**j & i]
    