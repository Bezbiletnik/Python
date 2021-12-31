def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target: return m
        elif nums[m] < target: l = m + 1
        else: r = m - 1
    if target > nums[m]: return m + 1
    else: return m
    

print(searchInsert(nums = [1,3,5,6], target = 2))