class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True


#Refactoring
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return (len(nums) != len(set(nums)))