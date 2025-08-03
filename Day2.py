from typing import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        # check frequency
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        total = count1 + count2

        # check it is possile
        for freq in total.values():
            if freq % 2 != 0:
                return -1
        
        # find extra fruits in basket
        extra1 = []
        extra2 = []

        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                extra1.extend([fruit] * (diff // 2))
            elif diff < 0:
                extra2.extend([fruit] * ((-diff) // 2))

        
        # finding minimum cost
        extra1.sort()
        extra2.sort(reverse=True)
        min_cost = min(total)
        cost = 0
        for a, b in zip(extra1, extra2):
            cost += min(min(a,b), min_cost*2) 
        
        return cost

sol = Solution()
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
print(sol.minCost(basket1, basket2))