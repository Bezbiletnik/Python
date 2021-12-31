# 1 solution
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return sum(max(accounts, key=lambda x: sum(x)))


# 2 solution
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0
        for i in accounts:
            if sum(i) > max:
                max = sum(i)
        return max


# Solution from Discusstions
# I didn't know that "map" function does like this 
def maximumWealth(self, accounts):
    return max(map(sum, accounts))