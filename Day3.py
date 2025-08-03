class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        max_fruits = 0
        total = 0
        left = 0

        for right in range(n):
            total += fruits[right][1]

            # Check if the window [left, right] is reachable within k steps
            while left <= right:
                print((left,right))
                leftPos = fruits[left][0]
                rightPos = fruits[right][0]

                # Calculate the minimal steps to visit [leftPos, rightPos] starting from startPos
                dist = min(
                    abs(startPos - leftPos) + (rightPos - leftPos),
                    abs(startPos - rightPos) + (rightPos - leftPos)
                )
                print(dist)

                if dist <= k:
                    break  # window is valid
                else:
                    total -= fruits[left][1]
                    left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits

sol = Solution()
fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
print(sol.maxTotalFruits(fruits, startPos, k))  # Output: 9
