from queue import Full

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1 or numRows > 30:
            return Full

        output = []
        for row_num in range(numRows):
            row = [1]

            if output:
                last_row = output[-1]
                for i in range(len(last_row)-1):
                    row.append(last_row[i] + last_row[i+1])
                    
                row.append(1)

            output.append(row)

        return output

sol = Solution()
numRows = 5
print(sol.generate(numRows))