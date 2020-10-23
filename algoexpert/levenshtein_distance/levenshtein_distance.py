def levenshteinDistance(str1, str2):
    """Find the edit distance between two strings."""
    str2, str1 = sorted((str1, str2), key=len)
    # After ith step, prefix_distance[j] represents the number of edits
    # required to transform str1[:i] into str2[:j]
    prefix_distance = list(range(len(str2)+1))
    for i in range(1, len(str1)+1):
        next_prefix_distance = [i] + len(str2)*[None]
        for j in range(1, len(str2)+1):
            next_prefix_distance[j] = min(
                prefix_distance[j] + 1,  # insertion
                next_prefix_distance[j-1] + 1, # deletion
                prefix_distance[j-1] + (str1[i-1] != str2[j-1]) # replacement
            )

        prefix_distance = next_prefix_distance

    return prefix_distance[-1]

################################

def memoize(func):
    """Memoize a function."""
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        
        return memo[args]

    return wrapper

@memoize
def levenshteinDistance1(str1, str2):
    """Find the edit distance between two strings.
    
    A memoized recursive implementation.
    """
    if '' in (str1, str2):
        return len(str1) or len(str2)

    return min(
        levenshteinDistance(str1, str2[:-1]) + 1,
        levenshteinDistance(str1[:-1], str2) + 1,
        levenshteinDistance(str1[:-1], str2[:-1]) + (str1[-1] != str2[-1])
    )


##############################

def levenshteinDistance2(str1, str2):
    """Find the edit distance between two strings."""
    str2, str1 = sorted([str1, str2], key=len)
    # After ith step, jth entry of prefix_dist is distance between
    # str2[:j] and str1[:i]. It is initialized to contain the edit
    # distance of prefixes to the empty string.\
    prefix_dist = list(range(len(str2)+1))
    for c in str1:
        new_prefix_dist = [None]*len(prefix_dist)
        last_c_appearance = None
        for split_point in range(len(prefix_dist)):
            new_prefix_dist[split_point] = prefix_dist[split_point] + 1
            if split_point > 0:
                new_prefix_dist[split_point] = min(
                    new_prefix_dist[split_point],
                    prefix_dist[split_point-1] + 1
                )
            if last_c_appearance is not None:
                new_prefix_dist[split_point] = min(
                    new_prefix_dist[split_point],
                    # pylint: disable=invalid-sequence-index
                    prefix_dist[last_c_appearance] + split_point - last_c_appearance - 1
                )

            if split_point < len(str2) and str2[split_point] == c:
                last_c_appearance = split_point

        prefix_dist = new_prefix_dist

    return prefix_dist[-1]

#################

@memoize
def levenshteinDistance3(str1, str2):
    """Find the edit distance between two strings."""
    if '' in (str1, str2):
        return _empty_string_dist(str1, str2)
    
    if len(str1) == 1:
        return _single_char_dist(str1, str2)

    for idx1 in range(len(str1)):
        sub_dist = float('inf')
        for idx2 in range(len(str2)+1):
            segment_1_dist = levenshteinDistance(str1[:idx1], str2[:idx2])
            segment_2_dist = levenshteinDistance(str1[idx1], str2[idx2:])

            sub_dist = min(sub_dist, segment_1_dist + segment_2_dist)

    return sub_dist
            
def _empty_string_dist(str1, str2):
    return max(len(str1), len(str2))

def _single_char_dist(a, str2):
    if str2 == '':
        return 1
    if a in str2:
        return len(str2)-1

    return len(str2)

def _empty_string_dist(str1, str2):
    return max(len(str1), len(str2))

def _single_char_dist(a, str2):
    if str2 == '':
        return 1
    if a in str2:
        return len(str2)-1

    return len(str2)
