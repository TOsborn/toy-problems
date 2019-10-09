class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        cost_list = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        max_length = 0
        lo = 0
        cost = 0
        for hi in range(len(s)):
            cost += cost_list[hi]
            while cost > max_cost:
                cost -= cost_list[lo]
                lo += 1

            max_length = max(hi - lo + 1, max_length)

        return max_length



f = Solution().equalSubstring
inputs = [
    ["abcd", "bcdf", 3],
    ["abcd", "cdef", 3],
    ["abcd", "acde", 0],

]
expected_outputs = [
    3,
    1,
    1,
]

for inp, outp in zip(inputs, expected_outputs):
    print(f(*inp), outp)
