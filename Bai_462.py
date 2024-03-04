class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        indexMedian = len(nums)//2
        median = nums[indexMedian]
        for num in nums:
            moves += abs(num - median)
        return moves