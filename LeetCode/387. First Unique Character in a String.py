# 1 Solution 
# The return statement is spoils everything
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = [i, 1]
            else:
                d[ch][1] += 1
        return -1 if all(x[1] != 1 for x in d.values()) else list(filter(lambda x: x[1] == 1, d.values()))[0][0]


# 2 Solution
# I thought that this solution will be worse than mine, but No
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chs = []
        for i in set(s):
            if s.count(i) == 1:
               chs.append(s.index(i))
        if len(chs) > 0:
            return min(chs)
        return -1


# 3 Solution
# That's very beautiful solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(char) for char in set(s) if s.count(char) == 1] or [-1])