# 1 Solution Complexity: TL: O(n) ML: O(n)
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = [0] * len(nums)
        for i in range(len(nums)):
            runningSum[i] = sum(nums[:i+1])
        return runningSum


# 2 Solution 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]


# 3 Solution Complexity: TL: O(n) ML: O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
