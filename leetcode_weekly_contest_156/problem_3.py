def change_to_counts(s):
    counts, vals = [], []
    if not s:
        return counts

    counts.append(1)
    vals.append(s[0])
    
    for i in range(1, len(s)):
        if s[i] == vals[-1]:
            counts[-1] += 1
        else:
            counts.append(1)
            vals.append(s[i])

    return counts, vals

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        counts, vals = change_to_counts(s)
        assert len(counts) == len(vals)

        pairs = [list(t) for t in zip(counts, vals)]
        changed = True
        while changed:
            if len(pairs) == 0:
                return ""
            
            length = len(pairs)
            new_pairs = [pairs[0]]
            for c, v in pairs[1:]:
                if v == new_pairs[-1][1]:
                    new_pairs[-1][0] += c
                else:
                    new_pairs.append([c, v])

            pairs = [[c % k, v] for c, v in new_pairs if c % k]
            changed = len(pairs) < length
            length = len(pairs)

        outstr = ""
        for c, v in pairs:
            outstr += c*v

        return outstr



            


f = Solution().removeDuplicates
inputs = [
    ["abcd", 2],
    ["deeedbbcccbdaa", 3],
    ["pbbcggttciiippooaais", 2]
]
expected_outputs = [
    "abcd",
    "aa",
    "ps",
]

for inp, outp in zip(inputs, expected_outputs):
    print(f(*inp), outp)