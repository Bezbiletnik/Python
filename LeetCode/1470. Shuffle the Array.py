# 1 Solution, brute force
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        for i,j in zip(nums[:n], nums[n:]):
            new_list.append(i); new_list.append(j)
        return new_list
