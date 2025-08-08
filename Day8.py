class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n >= 4800:
            return 1
        
        n = (n + 24) // 25

        # print(n)

        memory = {}

        def recursive_function(a,b):
            # print(a,b)
            if (a,b) in memory:
                return [(a,b)]
            
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0.0
            
            res = 0.25 * (recursive_function(a - 4, b) + recursive_function(a - 3, b - 1) + recursive_function(a - 2, b - 2) + recursive_function(a - 1, b - 3))
            memory[(a,b)] = res
            return res
        
        return recursive_function(n,n)

s = Solution()
print(s.soupServings(50))
print(s.soupServings(100))