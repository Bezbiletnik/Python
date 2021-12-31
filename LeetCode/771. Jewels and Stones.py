# 1 Solution TL: O(n * m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for x in stones if x in jewels])
                

# 2 Solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))


# 3 Solution
class Solution:
    def numJewelsInStones(self, J, S):
            setJ = set(J)
            return sum(s in setJ for s in S)