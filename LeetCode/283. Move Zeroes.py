def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for r in range(len(nums)):
        while nums[r] != 0 and l <= r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
    print(nums)

moveZeroes(nums = [1])