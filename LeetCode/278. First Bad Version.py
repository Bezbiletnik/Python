# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m+1): r = m
            else: l = m + 1
        return l+1