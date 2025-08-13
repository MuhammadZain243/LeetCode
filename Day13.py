class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # First Approach
        # if n < 1:
        #     return False
        
        # x = 0
        # result = 3 ** x

        # while result <= n:
        #     if result == n:
        #         return True
        #     x += 1
        #     result = 3 ** x

        # return False

        # Second Approach
        if n < 1:
            return False
        while n % 3 == 0 :
            n //= 3
        print(n)
        return n == 1

s = Solution()
# print(s.isPowerOfThree(27))
print(s.isPowerOfThree(9))
print(s.isPowerOfThree(2))