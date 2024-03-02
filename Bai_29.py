#Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dv = abs(dividend)
        d = abs(divisor)
        ans = 0
        while (dv >= d):
            tmp = d
            mul = 1
            while (dv >= tmp):
                dv = dv - tmp;
                ans += mul
                mul += mul
                tmp += tmp

        if (dividend >= 0 and divisor < 0) or (dividend <= 0 and divisor > 0):
            ans = -ans
        return min(2147483647, max(-2147483648, ans))
