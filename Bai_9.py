#Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        num = x
        sum = 0
        while (x != 0):
            mod = x % 10;
            sum = sum * 10 + mod
            x = x / 10
        if (num == sum):
            return True
        return False


