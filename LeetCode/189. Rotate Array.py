'''All codes with time limit exceeded work in other faster languages, but python is exception'''

'''My solution with "two pointers"'''
# Time Limit Exceeded
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1


# Easy solution
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


# Time limit Exceeded
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        a = nums[-1]
        for k in range(len(nums)):
            temp = nums[k]
            nums[k] = a
            a = temp


rotate(nums = [1,2,3,4,5,6,7], k = 3)