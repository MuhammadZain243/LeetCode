class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        i = 1
        while i <= n:
            if i == n:
                return True
            i <<= 1
        return False
    

s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(15))
print(s.isPowerOfTwo(4))