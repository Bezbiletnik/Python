# This alghorithm works only for sorted array


def twoSum(numbers: list[int], target: int) -> list[int]:
    r = len(numbers) - 1
    for l in range(len(numbers)):
        while l < r and numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] == target: return [l+1, r+1]
    return []


#Refactoring
def twoSum(numbers: list[int], target: int) -> list[int]:
    r = len(numbers) - 1
    l = 0
    while l < r:
        if  numbers[l] + numbers[r] == target: return [l+1, r+1]
        elif numbers[l] + numbers[r] > target: r -= 1
        else: l += 1
    return []


print(twoSum(numbers = [3, 2, 4], target = 6))
    