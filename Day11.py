MOD = 10**9 + 7

class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build powers array from binary representation
        powers = []
        bit = 1
        while n > 0:
            if n & 1:
                powers.append(bit)
            n >>= 1
            bit <<= 1

        # Step 2: Precompute prefix products (mod MOD)
        prefix = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD

        # Step 3: Answer queries using modular division
        def mod_inverse(x):
            # Fermat's little theorem (since MOD is prime)
            return pow(x, MOD - 2, MOD)

        ans = []
        for l, r in queries:
            product = (prefix[r + 1] * mod_inverse(prefix[l])) % MOD
            ans.append(product)

        return ans


# 🔎 Example Test Cases
s = Solution()
print(s.productQueries(15, [[0,1],[2,2],[0,3]]))  # [2, 4, 64]
print(s.productQueries(2, [[0,0]]))              # [2]
