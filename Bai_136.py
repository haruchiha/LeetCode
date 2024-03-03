class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
            # thao tac bit: XOR: a^a = 0; a^0 = a, a^b^c = a^c^b
        return ans
