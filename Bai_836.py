class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # SI = Max(0, Min(XA2, XB2) - Max(XA1, XB1)) * Max(0, Min(YA2, YB2) - Max(YA1, YB1))
        overWidth = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
        overHeight = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))
        if (overWidth * overHeight > 0):
            return True
        return False
