from functools import reduce

def arrayOfProducts(array):
    zero_index = None
    for i, a in enumerate(array):
        if a == 0:
            if zero_index:
                return [0]*len(array)

            zero_index = i

    if zero_index is not None:
        nonzero_entries = (a for i, a in enumerate(array) if i != zero_index)
        nonzero_product = reduce(lambda a, b: a*b, nonzero_entries)
        pre_length = zero_index
        post_length = len(array) - zero_index - 1
        return [0]*pre_length + [nonzero_product] + [0]*post_length

    product = reduce(lambda a, b: a*b, array)
    return [product // a for a in array]
