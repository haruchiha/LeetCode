class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        ans = 0
        if (k <= numOnes):
            ans = k
        if (k > numOnes and k - numOnes <= numZeros):
            ans = numOnes
        if (k > numOnes + numZeros):
            ans = 2 * numOnes + numZeros - k
        return ans
