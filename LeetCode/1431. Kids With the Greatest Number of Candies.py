# 1 Solution Complexity: TL: O(n) ML: O(n)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in candies:
            if i + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


# 2 Solution Complexity: TL: O(n) ML: O(1)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maximum:
                candies[i] = True
            else:
                candies[i] = False
        return candies


# 3 Solution TL: O(n) ML: O(n)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [candy + extraCandies >= maximum for candy in candies]