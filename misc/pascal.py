import math

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for n in xrange(numRows):
            row = []
            for i in xrange(n+1):
                row.append( math.factorial(n) / (math.factorial(n-i) * math.factorial(i)) )
            result.append(row)
        return result

print Solution().generate(0)
print Solution().generate(1)
print Solution().generate(2)
print Solution().generate(3)
