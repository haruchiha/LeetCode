class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        if a < b:
            for i in range (1, a+1):
                if(a % i == 0 and b % i == 0):
                    count += 1
        else:
            for i in range (1, b+1):
                if(a % i == 0 and b % i == 0):
                    count += 1
        return count