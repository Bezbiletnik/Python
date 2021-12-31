# 1 and 2 solutions a kinda bad, because they have TL: O(n*m)


# 1 Solution
# Passed 62 from 66 tests, Time Limit Exceeded
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s, j = list(s), 0
        for i in spaces:
            s.insert(i+j, ' ')
            j += 1
        return ''.join(s)


# 2 Solution
# Passed 58 from 66 tests, Time Limit Exceeded
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        new_str = ''
        for i in range(len(s)):
            if i in spaces:
                new_str += ' '
            new_str += s[i]
        return new_str


# 3 Solution TL: O(n), ML: O(n + m)
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result, j = [], 0
        for i, character in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(character)
        return ''.join(result)


# 4 Solution, same as 3, but with string
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str, j = '', 0
        for i, character in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                new_str += ' '
                j += 1
            new_str += character
        return new_str
