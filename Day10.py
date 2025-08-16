class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = sorted(str(n))   # sort the digits of n

        # Loop over powers of 2
        for i in range(30):
            power_of_two = 1 << i               # compute 2^i
            digits_sorted = sorted(str(power_of_two))  # sort its digits

            # Debugging prints (optional)
            print(f"i={i}, power_of_two={power_of_two}, digits_sorted={digits_sorted}")

            if target == digits_sorted:   # check if digits match
                return True

        return False


s = Solution()
print(s.reorderedPowerOf2(1))
# print(s.reorderedPowerOf2(10))