class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}  # Dictionary to store fruit type and its count
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            
            # Add the current fruit to the basket
            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1
            # print("Basket",basket)

            while len(basket) > 2:
                left_fruit = fruits[left]
                # print(left_fruit)
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            # print("Check Basket",basket)

            current_window = right - left + 1
            if current_window > max_fruits:
                max_fruits = current_window
                # print(max_fruits)
        return max_fruits

s = Solution()
# print(s.totalFruit([1, 2, 1]))        # Output: 3
print(s.totalFruit([0, 1, 2, 2]))     # Output: 3
# print(s.totalFruit([1, 2, 3, 2, 2]))  # Output: 4
