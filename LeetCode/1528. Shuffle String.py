# 1 Solution TL: O(n) ML: O(n)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = [0] * len(s)
        for i, ch in enumerate(indices):
            new_str[ch] = s[i]
        return ''.join(new_str)


# 2 Solution exactly the same
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        A = [''] * len(s)
        for i, j in zip(indices, s):
            A[i] = j
        return ''.join(A)
