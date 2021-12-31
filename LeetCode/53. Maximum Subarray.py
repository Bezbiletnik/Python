'''
    Kadane's algorithm


    Kadane's algorithm is used to find the maximum sum of a contiguous subarray.
    Kadane's algorithm is based on the idea of looking for all positive contiguous subarray and find the maximum sum of a contiguous subarray.
'''


# Not work for example with [-1]. Expected: -1, Output: 0
# As said in alghoritm 'for all positive contiguous subarray'


#Tests passed: 194 of 204
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum, current_sum = 0, 0
        for i in nums:
            current_sum += i
            if current_sum < 0:
                current_sum = 0
            if max_sum < current_sum:
                max_sum = current_sum
        return max_sum


# Solution
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximus, curr = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(curr+nums[i], nums[i])
            maximus = max(maximus, curr)
        return maximus