class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        number_str = list(str(num))

        for i in range(len(number_str)):
            if number_str[i] == '6':
                number_str[i] = '9'
                print(number_str)
                if int("".join(number_str)) > num:
                    num = int("".join(number_str))
                number_str[i] = '6'
        return num

s = Solution()
print(s.maximum69Number(9669))
