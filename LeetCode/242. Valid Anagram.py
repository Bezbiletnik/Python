from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return Counter(s) == Counter(t)
        return False


# It doesn't matter if len(s) and len(t) equal, so code will be like this:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
