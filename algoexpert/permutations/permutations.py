from math import factorial

def getPermutations(array):
    if len(array) == 0:
        return []
    
    if len(array) == 1:
        return [array]

    sub_perms = getPermutations(array[:-1])
    
    final_perms = []
    for insertion_idx in range(len(array)):
        for perm in sub_perms:
            perm_cpy = perm.copy()
            perm_cpy.insert(insertion_idx, array[-1])
            final_perms.append(perm_cpy)

    return final_perms

def getPermutations2(array):
    if array == []:
        return []

    perm_list = []
    for i in range(factorial(len(array))):
        perm = []
        for j in range(len(array)):
            insertion_idx = i % (j+1)
            i //= (j+1)
            perm.insert(insertion_idx, array[j])

        perm_list.append(perm)

    return perm_list
 