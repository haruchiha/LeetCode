class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        area2 = abs(bx1 - bx2) * abs(by1 - by2)
        total = area1 + area2
        overHeight = max(0, min(ax2, bx2) - max(ax1, bx1))
        overWidth = max(0, min(ay2, by2) - max(ay1, by1))
        overArea = overHeight * overWidth;

        return total - overArea;

        # Compute the area of the intersection, which is a rectangle too:
        # SI = Max(0, Min(XA2, XB2) - Max(XA1, XB1)) * Max(0, Min(YA2, YB2) - Max(YA1, YB1))
