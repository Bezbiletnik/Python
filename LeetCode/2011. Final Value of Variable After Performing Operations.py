class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0
        for operation in operations:
            if operation == '--X' or operation == 'X--':
                X -= 1
            else:
                X += 1
        return X


# Solution from Discuss
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum('+' in s or -1 for s in operations)