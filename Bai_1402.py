class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        temp = 0
        result = 0

        for s in satisfaction:
            temp += s
            if temp > 0:
                result += temp
            else:
                break
        return result


