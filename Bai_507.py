class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                if i * i != num:
                    sum = sum + num / i + i
                else:
                    sum = sum + i
        if sum == num and num != 1:
            return True
        return False
