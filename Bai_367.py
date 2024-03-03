class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = int(num**0.5)
        return ans*ans == num