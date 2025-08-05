class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n
        unplaces = 0

        # For Fuits
        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and fruits[i] <= baskets[j]:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaces += 1
        
        return unplaces


s = Solution()
print(s.numOfUnplacedFruits([4,2,5], [3,5,4]))
print(s.numOfUnplacedFruits([3,6,1], [6,4,7]))