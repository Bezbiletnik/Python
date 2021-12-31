import math

# My solution, but it's stupid. I math result(Complexity: O(1), but after I split result by '.' and take 2 part(Complexity: O(n)), because of
# log, that return value in float.
# Complexity: O(n)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else str(math.log2(n)).split('.')[1] == '0'


# My friend's solution
# Complexity O(log(n))
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        while n != 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True
        

# Solution from "Discusstions"
# Complexity: O(1)            
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # It's most beautiful solution
        # Logic: Because we have only 2^-31 < n < 2^31 - 1 the maximum power of 2 will be 30(1073741824), so we just need to check it
        return n > 0 and 1073741824 % n == 0