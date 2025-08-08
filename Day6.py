class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        used = [False] * len(baskets)
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced


s = Solution()
print(s.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))  # Output: 1
print(s.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))  # Output: 0
