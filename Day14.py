class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(9,0,-1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""
            

s = Solution()
print(s.largestGoodInteger("6777133339"))